# -*- coding: utf-8 -*-
from collections import OrderedDict
from MyWebSiteCreeper.entity.OnePieceCatalog import OnePieceCatalog
from MyWebSiteCreeper.dao.onepiecedao import OnePieceDao
import json
import scrapy
from scrapy.spiders import Spider
from scrapy.selector import Selector

class ShuhuiSpider(Spider):
    name = 'shuhui'
    allowed_domains = ['ishuhui.com']
    def __init__(self, *args,**kwargs):
        super(ShuhuiSpider,self).__init__(*args, **kwargs)

    #   先获取到完整漫画的所有话的id信息
    def parse(self, response):
        data=json.loads(response.body_as_unicode(), object_pairs_hook=OrderedDict)
        items=data['data']['cartoon']['0']['posts'].items()
        items=[OnePieceCatalog(int(p[0][2:]),p[1][0]['id'],p[1][0]['title'],p[1][0]['source']) for p in items]
        items=items[-1:-17:-1]
        for item in items:
            if item.source==1:
                if self.dao.saveInfo(item):
                    url='http://hhzapi.ishuhui.com/cartoon/post/ver/76906890/id/%s.json'%item.id
                    yield scrapy.Request(url,callback=self.parse_picList)
        print(items[0])

    #   再获取到每一话的图片url信息并下载
    def parse_picList(self, response):
        data = json.loads(response.body_as_unicode())
        picInfo=json.loads(data['data']['content_img'], object_pairs_hook=OrderedDict)
        orderlist=picInfo.items()
        keys=[p[0] for p in orderlist]
        self.dao.savePicOrderInfo(data['data']['number'],keys)
        urls=['http://hhzapi.ishuhui.com'+p[1] for p in orderlist]
        self.dao.save(urls, data['data']['number'])
