# using resolved_model self.resolved_model FIXME
# created from response, to create create_db_models.sqlite, with test data
#    that is used to create project
# should run without error in manager 
#    if not, check for decimal, indent, or import issues

import decimal
import logging
import sqlalchemy
from sqlalchemy.sql import func 
from decimal import Decimal
from logic_bank.logic_bank import Rule
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Numeric, Boolean, Text, DECIMAL
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from datetime import date   
from datetime import datetime
from typing import List


logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

Base = declarative_base()  # from system/genai/create_db_models_inserts/create_db_models_prefix.py


from sqlalchemy.dialects.sqlite import *

class AgileAIService(Base):
    """description: Represents the AI services offered by Agile AI Services company."""
    __tablename__ = 'agile_ai_services'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    platform = Column(String)

class Platform(Base):
    """description: Stores information about cloud platforms (AWS, Azure, GCP)."""
    __tablename__ = 'platforms'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)

class Specialty(Base):
    """description: Defines the specialties in which Agile AI Services operates."""
    __tablename__ = 'specialties'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Industry(Base):
    """description: Defines the industries (Healthcare, Hospitality) Agile AI Services focuses on."""
    __tablename__ = 'industries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class Product(Base):
    """description: Represents products developed for specific industries by Agile AI Services."""
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    agile_ai_service_id = Column(Integer, ForeignKey('agile_ai_services.id'))

class Configuration(Base):
    """description: Holds configuration settings for various products."""
    __tablename__ = 'configurations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    name = Column(String, nullable=False)
    value = Column(String)

class BlogPost(Base):
    """description: Tech blog posts written by Agile AI Services."""
    __tablename__ = 'blog_posts'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String)
    date_posted = Column(DateTime, default=datetime.now)

class HealthcareProduct(Base):
    """description: Special category for Healthcare-specific products."""
    __tablename__ = 'healthcare_products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    regulation_compliance = Column(String)

class HospitalityProduct(Base):
    """description: Special category for Hospitality-specific products."""
    __tablename__ = 'hospitality_products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    user_experiences = Column(String)

class ServiceSupport(Base):
    """description: Support services associated with Agile AI services."""
    __tablename__ = 'service_supports'
    id = Column(Integer, primary_key=True, autoincrement=True)
    agile_ai_service_id = Column(Integer, ForeignKey('agile_ai_services.id'))
    support_type = Column(String)
    details = Column(String)

class Customer(Base):
    """description: Customers who use Agile AI products."""
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    industry_id = Column(Integer, ForeignKey('industries.id'))
    product_id = Column(Integer, ForeignKey('products.id'))

class Deployment(Base):
    """description: Records of product deployments on various platforms."""
    __tablename__ = 'deployments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    platform_id = Column(Integer, ForeignKey('platforms.id'))
    deployment_date = Column(DateTime, default=datetime.now)
    status = Column(String)


# end of model classes


try:
    
    
    # ALS/GenAI: Create an SQLite database
    import os
    mgr_db_loc = True
    if mgr_db_loc:
        print(f'creating in manager: sqlite:///system/genai/temp/create_db_models.sqlite')
        engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
    else:
        current_file_path = os.path.dirname(__file__)
        print(f'creating at current_file_path: {current_file_path}')
        engine = create_engine(f'sqlite:///{current_file_path}/create_db_models.sqlite')
    Base.metadata.create_all(engine)
    
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # ALS/GenAI: Prepare for sample data
    
    
    session.commit()
    service1 = AgileAIService(
        name="AI Diagnostic Health",
        description="Cutting-edge AI diagnostics for healthcare",
        platform="AWS"
    )
    platform1 = Platform(
        name="AWS",
        description="Amazon Web Services Platform"
    )
    specialty1 = Specialty(
        name="Gen AI"
    )
    industry1 = Industry(
        name="Healthcare"
    )
    product1 = Product(
        name="AI Health Monitor",
        description="Monitor patient vitals through advanced AI algorithms",
        agile_ai_service_id=1
    )
    config1 = Configuration(
        product_id=1,
        name="High Sensitivity Mode",
        value="Enabled"
    )
    blog1 = BlogPost(
        title="The Future of AI in Healthcare",
        content="Exploring the latest developments in AI for the healthcare industry",
        date_posted=date(2023, 3, 15)
    )
    healthcare_prod1 = HealthcareProduct(
        product_id=1,
        regulation_compliance="FDA Approved"
    )
    hospitality_prod1 = HospitalityProduct(
        product_id=2,
        user_experiences="Enhanced Guest Interaction"
    )
    support1 = ServiceSupport(
        agile_ai_service_id=1,
        support_type="Premium Support",
        details="24/7 dedicated helpline"
    )
    customer1 = Customer(
        name="Global Health Corp",
        industry_id=1,
        product_id=1
    )
    deployment1 = Deployment(
        product_id=1,
        platform_id=1,
        deployment_date=date(2023, 2, 1),
        status="Deployed"
    )
    
    
    
    session.add_all([service1, platform1, specialty1, industry1, product1, config1, blog1, healthcare_prod1, hospitality_prod1, support1, customer1, deployment1])
    session.commit()
    # end of test data
    
    
except Exception as exc:
    print(f'Test Data Error: {exc}')
