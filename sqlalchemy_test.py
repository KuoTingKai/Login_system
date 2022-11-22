from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.sql.expression import values
from sqlalchemy.sql import select
from sqlalchemy import insert
from sqlalchemy import text
from sqlalchemy.sql import exists    


SQLALCHEMY_DATABASE_URL = "sqlite:///stock.db"

engine = create_engine('mysql+pymysql://root:cov45154551@localhost:3306/test')

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# class User(Base):
#     __tablename__ = 'tablename'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255))

#     def __init__(self, id=None, name=None):
#         self.id = id
#         self.name = name
def check(table,email=None,password=None):
    Session = sessionmaker(bind=engine)
    session = Session()

    if not email:
        return 'Please Enter Email'
    
    if not session.query(exists().where(table.c.Email == email)).scalar():
        return 'Email not exists'

    if not password:
        return 'Please Enter password'

    print(bool(session.query(user).filter_by(Email=email,Password=password).first()))
    # stmt = select(table.c.Password).where(table.c.Email == email)
    # conn = engine.connect()
    # result = conn.execute(stmt)
    # for i in result:
    #     print(i)
    #     if i == password:
    #         return True


    # return 

    # session.commit()     #提交會話（事務） 
    # session.rollback()     #回滾會話
    # session.close()     #關閉會話

def insert_value(table,email=None,password=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = user.insert().values(Email=email,Password=password)
    conn = engine.connect()
    conn.execute(ins)
    session.commit()     #提交會話（事務） 
    session.rollback()     #回滾會話
    session.close()     #關閉會話




def add(table, id, name):
    Session = sessionmaker(bind=engine)
    session = Session()
    table.id = id
    table.name = name
    session.commit()
    session.rollback()     #回滾會話
    session.close()     #關閉會話






# user = session.query(User).first()
# user.name = 'd'

# User.__table__.drop(engine)

# session.delete(user)
# session.query(user)
# session.add(user)
# create(session, User(4,'d'))
# session.commit()

# Session = sessionmaker(bind=engine)
# session = Session()
metadata = MetaData()
user = Table('user',Base.metadata,
			 Column('id', Integer(), primary_key=True), 
			 Column('Email', String(255), unique=True),
             Column('Password', String(255)) 
)
# metadata.create_all(engine)
# Base.metadata.create_all(engine)
# session.commit()     #提交會話（事務） 
# session.rollback()     #回滾會話
# session.close()     #關閉會話


# add(user,3,'a')


email = 'cov85741@gmail.com'
password = 'adsfe'
# 新增 > 查詢 > 
# insert_value(user,'cov85741@gmail.com','adsfes')
print(check(user,email,password))
