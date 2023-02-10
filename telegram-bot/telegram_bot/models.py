from datetime import datetime
from marshmallow import Schema, fields
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()


class SubDomain(Base):
    __tablename__ = "subdomain"
    id = Column(Integer, primary_key=True)
    domain_id = Column(Integer)
    subdomain = Column(String(255), unique=True)
    timestamp = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


class SubdomainSchema(Schema):
    class Meta:
        __model__ = SubDomain
        # load_instance = True
        # sqla_session = db.session


class Domain(Base):
    __tablename__ = "domain"
    id = Column(Integer, primary_key=True)
    domain = Column(String(255), unique=True)
    timestamp = Column(DateTime, default=datetime.now(), onupdate=datetime.now())


class DomainSchema(Schema):
    class Meta:
        __model__ = Domain
        # load_instance = True
        # sqla_session = db.session


domain_schema = DomainSchema()
domains_schema = DomainSchema(many=True)
subdomain_schema = SubdomainSchema()
subdomains_schema = SubdomainSchema(many=True)
