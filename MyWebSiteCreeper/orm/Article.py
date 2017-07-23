# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,ForeignKey,UniqueConstraint,Index,Text
from sqlalchemy.orm import relationship

#   创建对象的基类:
Base = declarative_base()

#   匹配文章的规则库
class ArticleRule(Base):
    # 表的名字:
    __tablename__ = 'articlerule'
    # 表的结构:
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(30))
    domains=Column(String(100))
    start_urls=Column(String(200))
    urls_types=Column(String(30))
    nextpage_xpath=Column(String(100))
    articleurl_xpath=Column(String(100))
    body_xpath=Column(String(100))
    title_xpath=Column(String(100))
    datetime_xpath=Column(String(100))
    sourcesite=Column(String(100))
    filter_xpath=Column(String(100))
    filter_regex=Column(String(100))
    minvalue=Column(Integer)
    enable=Column(Integer)

#   文章的类型
class ArticleType(Base):
    __tablename__ = 'articletype'
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String(100))

#   文章数据
class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content=Column(Text)
    contenttype=Column(Integer)
    posttime=Column(String(30))
    originUrl=Column(String(100))
    sourcesite=Column(String(100))
