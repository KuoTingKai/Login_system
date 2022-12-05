from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, MetaData, Table
from sqlalchemy.sql import exists    


SQLALCHEMY_DATABASE_URL = "sqlite:///stock.db"

engine = create_engine('mysql+pymysql://root:cov45154551@localhost:3306/test')

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = 'tablename'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))

    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name


def check(table,email=None,password=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    check_e = False
    check_p = False
    
    if session.query(exists().where(table.c.Email == email)).scalar():
        check_e = True
    else:
        check_e = False
        return check_e, check_p

    if session.query(table).filter_by(Email=email,Password=password).first():
        check_p = True
    else:
        check_p = False

    session.commit()     #提交會話（事務） 
    session.rollback()     #回滾會話
    session.close()     #關閉會話

    return check_e, check_p


def changePW(table,email=None,password=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    check_e = False
    check_p = False

    ins = table.update().values(Password=password).where(email == table.c.Email)
    conn = engine.connect()
    conn.execute(ins)
    # if session.query(exists().where(table.c.Email == email)).scalar():
    #     check_e = True
    # else:
    #     check_e = False
    #     return check_e, check_p

    session.commit()     #提交會話（事務） 
    session.rollback()     #回滾會話
    session.close()     #關閉會話
    return



def insert_value(table,email=None,password=None):
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = table.insert().values(Email=email,Password=password)
    conn = engine.connect()
    conn.execute(ins)
    session.commit()     #提交會話（事務） 
    session.rollback()     #回滾會話
    session.close()     #關閉會話




# def add(table, id, name):
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     table.id = id
#     table.name = name
#     session.commit()
#     session.rollback()     #回滾會話
#     session.close()     #關閉會話




# Session = sessionmaker(bind=engine)
# session = Session()

# metadata = MetaData()
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




# email = 'cov85741@gmail.com'
# password = 'adsfe'
# 新增 > 查詢 > 
# insert_value(user,'cov85741@gmail.com','adsfes')
# print(check(user,email,password))
