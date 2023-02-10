from datetime import datetime
from subfinder.config import db, ma


class SubDomain(db.Model):
    __tablename__ = "subdomain"
    id = db.Column(db.Integer, primary_key=True)
    domain_id = db.Column(db.Integer)
    subdomain = db.Column(db.String(255), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())


class SubdomainSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SubDomain
        load_instance = True
        sqla_session = db.session


class Domain(db.Model):
    __tablename__ = "domain"
    id = db.Column(db.Integer, primary_key=True)
    domain = db.Column(db.String(255), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())


class DomainSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Domain
        load_instance = True
        sqla_session = db.session


domain_schema = DomainSchema()
domains_schema = DomainSchema(many=True)
subdomain_schema = SubdomainSchema()
subdomains_schema = SubdomainSchema(many=True)
