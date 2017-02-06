from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
# from app import Base
Base = declarative_base()
engine = create_engine('postgresql://localhost/cmpe295')

#SQL design
class ImageMeta(Base):
	"""
	RDMS - table for image meta data
	"""

	__tablename__ = 'imagemeta'
	id = Column(Integer, primary_key = True)
	path = Column(String(100), nullable = False)
	preProcessed = Column(Boolean, nullable = False, default=False)
	createDate = Column(DateTime)

	def __init__(self, path, preProcesed):
		self.path = path
		self.preProcesed = preProcesed
		self.createDate = datetime.utcnow()

class UserData(Base):
	"""
	RDMS - table for user data
	"""

	__tablename__ = 'userdata'
	id = Column(Integer, primary_key = True)
	userName = Column(String(100), nullable = False)
	workType = Column(String(50), nullable = False)
	createDate = Column(DateTime)

	def __init__(self, userName, workType):
		self.userName = userName
		self.workType = workType
		self.createDate = datetime.utcnow()
