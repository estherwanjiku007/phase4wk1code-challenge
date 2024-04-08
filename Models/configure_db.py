from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
Metadata=MetaData()
db=SQLAlchemy(metadata=Metadata)