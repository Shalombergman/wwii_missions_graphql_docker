from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from based.base import Base
from models import *


#todo: can be converted to env variable via os.environ.get('DB_URL')
connection_url = "postgresql://admin:admin@psql-wwii:5432/missions_db"
engine = create_engine(connection_url, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

