# coding: utf-8
from sqlalchemy import DECIMAL, DateTime  # API Logic Server GenAI assist
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

########################################################################################################################
# Classes describing database for SqlAlchemy ORM, initially created by schema introspection.
#
# Alter this file per your database maintenance policy
#    See https://apilogicserver.github.io/Docs/Project-Rebuild/#rebuilding
#
# Created:  January 31, 2025 00:02:38
# Database: sqlite:////tmp/tmp.Nu2wF0cKqM-01JJWTKM873G4R1ZDRQRXRZ8NN/AgileAI_DB_Schema/database/db.sqlite
# Dialect:  sqlite
#
# mypy: ignore-errors
########################################################################################################################
 
from database.system.SAFRSBaseX import SAFRSBaseX, TestBase
from flask_login import UserMixin
import safrs, flask_sqlalchemy, os
from safrs import jsonapi_attr
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.sql.sqltypes import NullType
from typing import List

db = SQLAlchemy() 
Base = declarative_base()  # type: flask_sqlalchemy.model.DefaultMeta
metadata = Base.metadata

#NullType = db.String  # datatype fixup
#TIMESTAMP= db.TIMESTAMP

from sqlalchemy.dialects.sqlite import *

if os.getenv('APILOGICPROJECT_NO_FLASK') is None or os.getenv('APILOGICPROJECT_NO_FLASK') == 'None':
    Base = SAFRSBaseX   # enables rules to be used outside of Flask, e.g., test data loading
else:
    Base = TestBase     # ensure proper types, so rules work for data loading
    print('*** Models.py Using TestBase ***')



class AgileAiService(Base):  # type: ignore
    """
    description: Represents the AI services offered by Agile AI Services company.
    """
    __tablename__ = 'agile_ai_services'
    _s_collection_name = 'AgileAiService'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    platform = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    ProductList : Mapped[List["Product"]] = relationship(back_populates="agile_ai_service")
    ServiceSupportList : Mapped[List["ServiceSupport"]] = relationship(back_populates="agile_ai_service")



class BlogPost(Base):  # type: ignore
    """
    description: Tech blog posts written by Agile AI Services.
    """
    __tablename__ = 'blog_posts'
    _s_collection_name = 'BlogPost'  # type: ignore

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String)
    date_posted = Column(DateTime)

    # parent relationships (access parent)

    # child relationships (access children)



class Industry(Base):  # type: ignore
    """
    description: Defines the industries (Healthcare, Hospitality) Agile AI Services focuses on.
    """
    __tablename__ = 'industries'
    _s_collection_name = 'Industry'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)
    CustomerList : Mapped[List["Customer"]] = relationship(back_populates="industry")



class Platform(Base):  # type: ignore
    """
    description: Stores information about cloud platforms (AWS, Azure, GCP).
    """
    __tablename__ = 'platforms'
    _s_collection_name = 'Platform'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

    # parent relationships (access parent)

    # child relationships (access children)
    DeploymentList : Mapped[List["Deployment"]] = relationship(back_populates="platform")



class Specialty(Base):  # type: ignore
    """
    description: Defines the specialties in which Agile AI Services operates.
    """
    __tablename__ = 'specialties'
    _s_collection_name = 'Specialty'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # parent relationships (access parent)

    # child relationships (access children)



class Product(Base):  # type: ignore
    """
    description: Represents products developed for specific industries by Agile AI Services.
    """
    __tablename__ = 'products'
    _s_collection_name = 'Product'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    agile_ai_service_id = Column(ForeignKey('agile_ai_services.id'))

    # parent relationships (access parent)
    agile_ai_service : Mapped["AgileAiService"] = relationship(back_populates=("ProductList"))

    # child relationships (access children)
    ConfigurationList : Mapped[List["Configuration"]] = relationship(back_populates="product")
    CustomerList : Mapped[List["Customer"]] = relationship(back_populates="product")
    DeploymentList : Mapped[List["Deployment"]] = relationship(back_populates="product")
    HealthcareProductList : Mapped[List["HealthcareProduct"]] = relationship(back_populates="product")
    HospitalityProductList : Mapped[List["HospitalityProduct"]] = relationship(back_populates="product")



class ServiceSupport(Base):  # type: ignore
    """
    description: Support services associated with Agile AI services.
    """
    __tablename__ = 'service_supports'
    _s_collection_name = 'ServiceSupport'  # type: ignore

    id = Column(Integer, primary_key=True)
    agile_ai_service_id = Column(ForeignKey('agile_ai_services.id'))
    support_type = Column(String)
    details = Column(String)

    # parent relationships (access parent)
    agile_ai_service : Mapped["AgileAiService"] = relationship(back_populates=("ServiceSupportList"))

    # child relationships (access children)



class Configuration(Base):  # type: ignore
    """
    description: Holds configuration settings for various products.
    """
    __tablename__ = 'configurations'
    _s_collection_name = 'Configuration'  # type: ignore

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    name = Column(String, nullable=False)
    value = Column(String)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("ConfigurationList"))

    # child relationships (access children)



class Customer(Base):  # type: ignore
    """
    description: Customers who use Agile AI products.
    """
    __tablename__ = 'customers'
    _s_collection_name = 'Customer'  # type: ignore

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    industry_id = Column(ForeignKey('industries.id'))
    product_id = Column(ForeignKey('products.id'))

    # parent relationships (access parent)
    industry : Mapped["Industry"] = relationship(back_populates=("CustomerList"))
    product : Mapped["Product"] = relationship(back_populates=("CustomerList"))

    # child relationships (access children)



class Deployment(Base):  # type: ignore
    """
    description: Records of product deployments on various platforms.
    """
    __tablename__ = 'deployments'
    _s_collection_name = 'Deployment'  # type: ignore

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    platform_id = Column(ForeignKey('platforms.id'))
    deployment_date = Column(DateTime)
    status = Column(String)

    # parent relationships (access parent)
    platform : Mapped["Platform"] = relationship(back_populates=("DeploymentList"))
    product : Mapped["Product"] = relationship(back_populates=("DeploymentList"))

    # child relationships (access children)



class HealthcareProduct(Base):  # type: ignore
    """
    description: Special category for Healthcare-specific products.
    """
    __tablename__ = 'healthcare_products'
    _s_collection_name = 'HealthcareProduct'  # type: ignore

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    regulation_compliance = Column(String)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("HealthcareProductList"))

    # child relationships (access children)



class HospitalityProduct(Base):  # type: ignore
    """
    description: Special category for Hospitality-specific products.
    """
    __tablename__ = 'hospitality_products'
    _s_collection_name = 'HospitalityProduct'  # type: ignore

    id = Column(Integer, primary_key=True)
    product_id = Column(ForeignKey('products.id'))
    user_experiences = Column(String)

    # parent relationships (access parent)
    product : Mapped["Product"] = relationship(back_populates=("HospitalityProductList"))

    # child relationships (access children)
