from findomain.config import app, db
from findomain.models import Domain, domain_schema, domains_schema


# Lấy ra tất cả các domain trong db
def read_all_domain():
    with app.app_context():
        domains = Domain.query.all()
        if domains is not None:
            return domains_schema.dump(domains)
        else:
            return None


# Lấy ra một domain trong db
def read_one_domain(domain_id):
    with app.app_context():
        domain = Domain.query.get(domain_id)
        if domain is not None:
            return domain_schema.dump(domain)
        else:
            return None


# Tạo mới một domain
def create_one_domain(data):
    # data = {'domain': 'example.local'}
    with app.app_context():
        domain = data.get("domain")
        existing_domain = Domain.query.filter(Domain.domain == domain).one_or_none()
        if existing_domain is None:
            new_domain = domain_schema.load(data, session=db.session)
            db.session.add(new_domain)
            db.session.commit()
            return True
        else:
            return False
