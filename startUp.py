# coding:utf-8
from MyWebSiteCreeper.spiders.onepieceSpider import OnepieceSpider
from MyWebSiteCreeper.spiders.yinhunSpider import YinhunSpider
from MyWebSiteCreeper.spiders.articleSpider import ArticleSpider
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from MyWebSiteCreeper.dao.articledao import ArticleDao
import copy

settings = get_project_settings()
configure_logging(settings)
runner = CrawlerRunner(settings)

#runner.crawl(OnepieceSpider)
#runner.crawl(YinhunSpider)

# import os
# os.system('scrapy crawl onepiece')

dao=ArticleDao()
rules=dao.findAllRules()
ArticleSpider.all_urls=set(dao.findAllAricleUrls())
for rule in rules:
    if rule.enable:
        sts=rule.start_urls.split(',')
        tps=rule.urls_types.split(',')
        for i in range(len(sts)):
            rl=copy.deepcopy(rule)
            rl.start_urls=sts[i]
            rl.urls_types=tps[i]
            runner.crawl(ArticleSpider,rule=rl)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
