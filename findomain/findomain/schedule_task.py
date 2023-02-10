import os
import time
import requests
import subprocess

from datetime import datetime
from flask_apscheduler import APScheduler

from findomain.logging import logger
from findomain.domain import read_all_domain
from findomain.config import BINS_DIR, DATA_DIR, FINDOMAIN_BIN, BOT_TOKEN, CHAT_ID
from findomain.subdomain import create_one_subdomain, read_all_subdomain_by_domain_id


# Ghi lại kết quả các subdomain tìm thấy ra file
def findomain_log_to_file(domain_name, data_list):
    try:
        today = datetime.today()
        path = os.path.join(DATA_DIR, domain_name, str(today.year), str(today.month))
        filename = f"{str(today.day)}-{today.hour}{today.minute}{today.second}" + ".txt"
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        with open(os.path.join(path, filename), "w") as f:
            for data in data_list:
                f.write(f"{data}\n")
    except Exception as ex:
        logger.warning(str(ex))
        return False
    else:
        return True


# Gửi alert qua telegram
def findomain_send_telegram(text):
    try:
        token = BOT_TOKEN
        chat_id = CHAT_ID
        text = f"[Findomain][New SubDomain]:\n{text}"
        api_url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&parse_mode=Markdown&text=`{text}`"
        response = requests.get(api_url)
    except Exception as ex:
        logger.warning(str(ex))
    else:
        return response.json()


# Tìm kiếm các subdomain
def findomain_discovery(domain):
    try:
        domains = []
        findomain_bin = os.path.join(BINS_DIR, FINDOMAIN_BIN)
        findomain_cmd = [findomain_bin, "-q", "-t", domain]
        findomain_output = subprocess.run(findomain_cmd, stdout=subprocess.PIPE)
        temp = findomain_output.stdout.decode().splitlines()
        for dm in temp:
            if len(dm) > 0:
                if dm.startswith("www."):
                    dm = dm.replace("www.", "")
                domains.append(dm)
        domains = list(set(domains))
    except Exception as ex:
        logger.warning(str(ex))
    else:
        return domains


def findomain_task():
    try:
        # Lấy danh sách các domain đang monitor trong db
        domains = read_all_domain()
        if domains is None:
            logger.warning("Domain list is None")
            return

        # Tìm kiếm các subdomain cho từng domain đã lấy ra
        for item in domains:
            domain = item.get("domain")
            domain_id = item.get("id")

            logger.warning(f"Subdomain discovery for: {domain}")
            subdomains_found = findomain_discovery(domain)

            # Ghi logs ra file các subdomain tìm được
            if findomain_log_to_file(domain, subdomains_found):
                logger.warning(f"Total found {len(subdomains_found)} subdomain for '{domain}'")
            else:
                logger.warning("Logs to file failed!")

            tmp_subdomain = read_all_subdomain_by_domain_id(item)
            subdomains_in_db = []
            for sub in tmp_subdomain:
                subdomains_in_db.append(sub.get("subdomain"))

            # Lọc ra những subdomain chưa có trong db
            subdomain_not_in_db = list(set(subdomains_found) - set(subdomains_in_db))

            # Ghi logs và cảnh báo qua telegram
            num_of_new_subdomain = len(subdomain_not_in_db)
            if num_of_new_subdomain > 0:
                logger.warning(f"Found {num_of_new_subdomain} new subdomain for '{domain}': {str(subdomain_not_in_db)}")
                batch_size = 10
                for i in range(0, len(subdomain_not_in_db), batch_size):
                    batch_subdomain = subdomain_not_in_db[i:i + batch_size]
                    rsp = findomain_send_telegram(str(batch_subdomain))
                    time.sleep(1)
                    logger.warning(f"Successful send to telegram: {str(rsp)}")

                # Cập nhật vào db các subdomain mới
                for sdm in subdomain_not_in_db:
                    new_subdomain = {"domain_id": domain_id, "subdomain": sdm}
                    if create_one_subdomain(new_subdomain):
                        logger.warning("Successful update to db")
                        time.sleep(0.5)
                    else:
                        logger.warning("Failed to update db!")
            else:
                logger.warning(f"Nothing found new subdomain for '{domain}'")
    except Exception as ex:
        logger.warning(str(ex))
    else:
        return None


def schedule_task():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.warning(f"{now} - Starting a schedule job")
    findomain_task()


def schedule_start():
    scheduler = APScheduler()
    scheduler.add_job(id='Scheduled Task', func=schedule_task, trigger="interval", hours=12)
    scheduler.start()
