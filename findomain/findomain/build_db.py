#!/usr/bin/env python

from findomain.config import app, db
from findomain.models import Domain, SubDomain

# Dinh nghia du lieu tam
DOMAINS = [
    {"id": 1, "domain": "vccorp.vn"},
    {"id": 2, "domain": "bizflycloud.vn"}
]

SUBDOMAIN = [
    {"id": 1, "domain_id": 1, "subdomain": "salary.vccorp.vn"},
    {"id": 2, "domain_id": 1, "subdomain": "bonus.vccorp.vn"},
    {"id": 3, "domain_id": 2, "subdomain": "dichvu.bizflycloud.vn"},
    {"id": 4, "domain_id": 2, "subdomain": "gate.bizflycloud.vn"}
]


# Tao du lieu tam cho db
def build_db():
    with app.app_context():
        db.drop_all()
        db.create_all()
        for dm in DOMAINS:
            new_dm = Domain(domain=dm.get("domain"))
            db.session.add(new_dm)
        db.session.commit()
        for sdm in SUBDOMAIN:
            new_sdm = SubDomain(domain_id=sdm.get("domain_id"), subdomain=sdm.get("subdomain"))
            db.session.add(new_sdm)
        db.session.commit()


if __name__ == "__main__":
    build_db()
