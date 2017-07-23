# -*- coding: utf-8 -*-
import os
from MyWebSiteCreeper.spiders import shuhuiSpider
from MyWebSiteCreeper.dao.onepiecedao import OnePieceDao
class YinhunSpider(shuhuiSpider.ShuhuiSpider):
    name = 'yinhun'
    allowed_domains = ['ishuhui.com']
    def __init__(self, *args, **kwargs):
        super(YinhunSpider, self).__init__(*args, **kwargs)
        shuhuipath = os.path.abspath('../data/银魂')
        self.dao = OnePieceDao(shuhuipath)
        self.start_urls = [
            'http://api.ishuhui.com/cartoon/book_ish/ver/23017113/id/2.json'
        ]
        self.dao.deletePrevious()  # 每次爬之前只保留最近下载的16话
