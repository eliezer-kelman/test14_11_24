from sqlalchemy.orm import declarative_base
Base = declarative_base()


from .user import User
from .device import Device
from .location import Location
from .suspicious_hostage_content import SuspiciousHostageContent
from .suspicious_explosive_content import SuspiciousExplosiveContent
from .full_message import FullMessage