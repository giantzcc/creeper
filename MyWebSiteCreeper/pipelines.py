# -*- coding: utf-8 -*-
from MyWebSiteCreeper.dao.articledao import ArticleDao
from MyWebSiteCreeper.orm.Article import Article
from MyWebSiteCreeper.items import ArticleItem
import functools
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#   定义一个装饰器用于区分保存不同spider抓来的数据
def SplitPipeline(func):
    def decorator(*arg,**kw):
        if isinstance(arg[1],arg[0].type):
            func(*arg, **kw)
    return decorator

class ArticlePipeline(object):
    dao = ArticleDao()
    def __init__(self):
        self.type=ArticleItem
    @SplitPipeline
    def process_item(self, item, spider):
        piece=Article(title=item['title'],content=item['body'].encode('utf-8'),contenttype=item['content_type'],posttime=item['publish_time'],originUrl=item['url'],sourcesite=item['source_site'])
        self.dao.add(piece)

