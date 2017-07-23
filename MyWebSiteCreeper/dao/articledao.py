# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from MyWebSiteCreeper.orm.Article import Article,ArticleRule,ArticleType
from contextlib import contextmanager

#   定义适用于session的with语句 相当于事务切面
@contextmanager
def session_scope(Session):
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

class ArticleDao(object):
    def __init__(self):
        # 初始化数据库连接:
        engine = create_engine('mysql+pymysql://root:root@localhost:3306/mywebsite?charset=utf8')
        # 创建DBSession类型:
        self.DBSession = sessionmaker(bind=engine)

    #   保存多篇文章
    def addAll(self,articles):
        with session_scope(self.DBSession) as session:
            session.add_all(articles)

    #   保存一篇文章
    def add(self,article):
        with session_scope(self.DBSession) as session:
            session.add(article)

    #   返回所有的规则
    def findAllRules(self):
        rst=[]
        session = self.DBSession()
        try:
            rst=session.query(ArticleRule).all()
        finally:
            session.close()
            return rst

    #   返回所有文章的url
    def findAllAricleUrls(self):
        rst = []
        session = self.DBSession()
        try:
            rst=session.query(Article.originUrl).all()
            rst=[x.originUrl for x in rst]
        finally:
            session.close()
        return rst