# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,Index
from sqlalchemy.orm import relationship

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

    # 一对多:
    #books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20), ForeignKey('user.id'))
    user=relationship('User')

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:root@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建Session:
session = DBSession()
bk=session.query(Book).filter(Book.id==3).one()
print(bk.name)
print(bk.user_id)
print(bk.user.name)
session.commit()
# 关闭Session:
session.close()