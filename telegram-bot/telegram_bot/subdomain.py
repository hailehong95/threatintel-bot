from subfinder.config import app, db
from subfinder.models import SubDomain, subdomain_schema, subdomains_schema


# Lấy ra tất cả các subdomain trong db
def read_all_subdomain():
    with app.app_context():
        subdomains = SubDomain.query.all()
        if subdomains is not None:
            return subdomains_schema.dump(subdomains)
        else:
            return None


# Lấy ra tất cả các subdomain có cùng domain_id trong db
def read_all_subdomain_by_domain_id(data):
    # data = {'id': 1, 'domain': 'example.local'}
    with app.app_context():
        domain_id = data.get("id")
        subdomains = SubDomain.query.filter(SubDomain.domain_id == domain_id).all()
        if subdomains is not None:
            return subdomains_schema.dump(subdomains)
        else:
            return None


# Lấy ra một subdomain trong db theo id của subdomain
def read_one_subdomain(subdomain_id):
    with app.app_context():
        subdomain = SubDomain.query.get(subdomain_id)
        if subdomain is not None:
            return subdomain_schema.dump(subdomain)
        else:
            return None


# Tạo mới một subdomain
def create_one_subdomain(data):
    # data = {'domain_id': 1, 'subdomain': 'sub.example.local'}
    with app.app_context():
        subdomain = data.get("subdomain")
        existing_subdomain = SubDomain.query.filter(SubDomain.subdomain == subdomain).one_or_none()
        if existing_subdomain is None:
            new_subdomain = subdomain_schema.load(data, session=db.session)
            db.session.add(new_subdomain)
            db.session.commit()
            return True
        else:
            return False
