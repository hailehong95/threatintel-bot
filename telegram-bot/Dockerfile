#FROM ubuntu:20.04
#WORKDIR /threatintel-bot
#COPY requirements.txt /threatintel-bot
#RUN apt update -y
#RUN apt install -y build-essential libssl-dev libffi-dev python3 python3-dev python3-pip
#RUN pip3 install -r requirements.txt --no-cache-dir
#COPY . /threatintel-bot
#ENTRYPOINT ["python3"]
#CMD ["telegram_bot.py"]

FROM python:3.10-alpine

WORKDIR /app

RUN apk update && apk upgrade --no-cache
RUN apk add gcc musl-dev mariadb-connector-c-dev
RUN apk add --no-cache tzdata
ENV TZ=Asia/Ho_Chi_Minh

COPY requirements.txt /app
RUN pip install -r requirements.txt --no-cache-dir
COPY . /app

ENTRYPOINT ["python"]
CMD ["telegram_bot.py"]
