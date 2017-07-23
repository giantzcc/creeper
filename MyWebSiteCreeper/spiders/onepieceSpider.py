# -*- coding: utf-8 -*-
import os
from MyWebSiteCreeper.spiders import shuhuiSpider
from MyWebSiteCreeper.dao.onepiecedao import OnePieceDao
class OnepieceSpider(shuhuiSpider.ShuhuiSpider):
    name='onepiece'
    allowed_domains=['ishuhui.com']
    def __init__(self, *args, **kwargs):
        super(OnepieceSpider,self).__init__(*args,**kwargs)
        shuhuipath=os.path.abspath('../data/海贼王')
        self.dao=OnePieceDao(shuhuipath)
        self.start_urls = [
            'http://api.ishuhui.com/cartoon/book_ish/ver/23017113/id/1.json'
        ]
        self.dao.deletePrevious()  # 每次爬之前只保留最近下载的16话
