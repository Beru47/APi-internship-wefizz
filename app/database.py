from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:haythoum@localhost/api_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionLocal = sessionmaker(autocommit = False,  autoflush= False, bind=engine)
Base = declarative_base()

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
<<<<<<< HEAD
        db.close()
        
=======
        db.close()
>>>>>>> 0f7c17036686660adfbbe85d8083e8ecebac0bc5
