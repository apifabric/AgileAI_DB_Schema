import logging
import logging.config
import json
import os
import sys

os.environ["APILOGICPROJECT_NO_FLASK"] = "1"  # must be present before importing models

import traceback
import yaml
from datetime import date, datetime
from pathlib import Path
from decimal import Decimal
from sqlalchemy import (Boolean, Column, Date, DateTime, DECIMAL, Float, ForeignKey, Integer, Numeric, String, Text, create_engine)
from sqlalchemy.dialects.sqlite import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

current_path = Path(__file__)
project_path = (current_path.parent.parent.parent).resolve()
sys.path.append(str(project_path))

from logic_bank.logic_bank import LogicBank, Rule
from logic import declare_logic
from database.models import *
from database.models import Base

project_dir = Path(os.getenv("PROJECT_DIR",'./')).resolve()

assert str(os.getcwd()) == str(project_dir), f"Current directory must be {project_dir}"

data_log : list[str] = []

logging_config = project_dir / 'config/logging.yml'
if logging_config.is_file():
    with open(logging_config,'rt') as f:  
        config=yaml.safe_load(f.read())
    logging.config.dictConfig(config)
logic_logger = logging.getLogger('logic_logger')
logic_logger.setLevel(logging.DEBUG)
logic_logger.info(f'..  logic_logger: {logic_logger}')

db_url_path = project_dir.joinpath('database/test_data/db.sqlite')
db_url = f'sqlite:///{db_url_path.resolve()}'
logging.info(f'..  db_url: {db_url}')
logging.info(f'..  cwd: {os.getcwd()}')
logging.info(f'..  python_loc: {sys.executable}')
logging.info(f'..  test_data_loader version: 1.1')
data_log.append(f'..  db_url: {db_url}')
data_log.append(f'..  cwd: {os.getcwd()}')
data_log.append(f'..  python_loc: {sys.executable}')
data_log.append(f'..  test_data_loader version: 1.1')

if db_url_path.is_file():
    db_url_path.unlink()

try:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)  # note: LogicBank activated for this session only
    session = Session()
    LogicBank.activate(session=session, activator=declare_logic.declare_logic)
except Exception as e: 
    logging.error(f'Error creating engine: {e}')
    data_log.append(f'Error creating engine: {e}')
    print('\n'.join(data_log))
    with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
        log_file.write('\n'.join(data_log))
    print('\n'.join(data_log))
    raise

logging.info(f'..  LogicBank activated')
data_log.append(f'..  LogicBank activated')

restart_count = 0
has_errors = True
succeeded_hashes = set()

while restart_count < 5 and has_errors:
    has_errors = False
    restart_count += 1
    data_log.append("print(Pass: " + str(restart_count) + ")" )
    try:
        if not 6495900871731228805 in succeeded_hashes:  # avoid duplicate inserts
            instance = service1 = AgileAIService(
    name="AI Diagnostic Health",
    description="Cutting-edge AI diagnostics for healthcare",
    platform="AWS"
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6495900871731228805)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 3927022604134569946 in succeeded_hashes:  # avoid duplicate inserts
            instance = platform1 = Platform(
    name="AWS",
    description="Amazon Web Services Platform"
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(3927022604134569946)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4302484432946841320 in succeeded_hashes:  # avoid duplicate inserts
            instance = specialty1 = Specialty(
    name="Gen AI"
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4302484432946841320)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 2335837346796692555 in succeeded_hashes:  # avoid duplicate inserts
            instance = industry1 = Industry(
    name="Healthcare"
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(2335837346796692555)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 5934071005770633946 in succeeded_hashes:  # avoid duplicate inserts
            instance = product1 = Product(
    name="AI Health Monitor",
    description="Monitor patient vitals through advanced AI algorithms",
    agile_ai_service_id=1
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(5934071005770633946)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4442386629511964177 in succeeded_hashes:  # avoid duplicate inserts
            instance = config1 = Configuration(
    product_id=1,
    name="High Sensitivity Mode",
    value="Enabled"
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4442386629511964177)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -4819167738809601710 in succeeded_hashes:  # avoid duplicate inserts
            instance = blog1 = BlogPost(
    title="The Future of AI in Healthcare",
    content="Exploring the latest developments in AI for the healthcare industry",
    date_posted=date(2023, 3, 15)
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-4819167738809601710)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not -1084795107015988264 in succeeded_hashes:  # avoid duplicate inserts
            instance = healthcare_prod1 = HealthcareProduct(
    product_id=1,
    regulation_compliance="FDA Approved"
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(-1084795107015988264)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 4452120304116827698 in succeeded_hashes:  # avoid duplicate inserts
            instance = hospitality_prod1 = HospitalityProduct(
    product_id=2,
    user_experiences="Enhanced Guest Interaction"
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(4452120304116827698)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 7455168078458489595 in succeeded_hashes:  # avoid duplicate inserts
            instance = support1 = ServiceSupport(
    agile_ai_service_id=1,
    support_type="Premium Support",
    details="24/7 dedicated helpline"
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(7455168078458489595)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 6952335052006357559 in succeeded_hashes:  # avoid duplicate inserts
            instance = customer1 = Customer(
    name="Global Health Corp",
    industry_id=1,
    product_id=1
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(6952335052006357559)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()

    try:
        if not 8101707569589706276 in succeeded_hashes:  # avoid duplicate inserts
            instance = deployment1 = Deployment(
    product_id=1,
    platform_id=1,
    deployment_date=date(2023, 2, 1),
    status="Deployed"
)
            session.add(instance)
            session.commit()
            succeeded_hashes.add(8101707569589706276)
    except Exception as e:
        has_errors = True
        if 'UNIQUE' in str(e) and restart_count > 1:
            pass
        else:
            error_str = f"Error adding variable to session: {e}"
            if not error_str in data_log:
                data_log.append(error_str)
        if not restart_count in [2,3]:
            session.rollback()
print('\n'.join(data_log))
with open(project_dir / 'database/test_data/test_data_code_log.txt', 'w') as log_file:
    log_file.write('\n'.join(data_log))
print('\n'.join(data_log))
