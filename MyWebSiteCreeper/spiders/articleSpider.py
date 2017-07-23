# -*- coding: utf-8 -*-
import scrapy
import re
from MyWebSiteCreeper.items import ArticleItem
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from MyWebSiteCreeper.orm.Article import Article
#str(rule.max_count)
class ArticleSpider(CrawlSpider):
    # custom_settings = {
    #     'CLOSESPIDER_ITEMCOUNT':20
    # }
    def __init__(self,rule):
        self.rule=rule
        self.name=rule.name
        self.allowed_domains=rule.domains.split(',')
        self.start_urls=[rule.start_urls]
        rule_list=[]
        #if rule.nextpage_xpath:
        #    rule_list.append(Rule(LinkExtractor(restrict_xpaths=[rule.nextpage_xpath])))
        #rule_list.append(Rule(LinkExtractor(restrict_xpaths=[rule.articleurl_xpath]),
        #                      callback='parseArticle'))
        #self.rules=tuple(rule_list)
        super(ArticleSpider,self).__init__()

    def parse(self,response):
        print(response.url)
        urls=response.xpath(self.rule.articleurl_xpath).extract()
        filter = []
        if self.rule.filter_xpath:
            totals=response.xpath(self.rule.filter_xpath).extract()
            dt=[]
            for t in totals:
                gps=re.findall(self.rule.filter_regex,t)
                dt.append(''.join(gps))
            for index in range(len(dt)):
                if int(dt[index])>=self.rule.minvalue:
                    filter.append(index)
        else:
            filter=list(range(len(urls)))
        for index in filter:
            if not urls[index].startswith('http'):
                urls[index]=urls[index][urls[index].index('/'):]
                urls[index]='http://'+self.allowed_domains[0]+urls[index]
            yield scrapy.Request(urls[index], callback=self.parse_item)
        nextpage=response.xpath(self.rule.nextpage_xpath).extract()
        for url in nextpage:
            if not url.startswith('http'):
                url=url[url.index('/'):]
                url='http://'+self.allowed_domains[0]+url
            yield scrapy.Request(url, callback=self.parse)

    def parse_item(self,response):
        print('Article from %s ' % response.url)
        print('Title:%s' % response.xpath(self.rule.title_xpath).extract())
        print('Date:%s' % response.xpath(self.rule.datetime_xpath).extract())
        article=ArticleItem()
        article['url']=response.url
        article['title']=''.join(response.xpath(self.rule.title_xpath).extract())
        article['publish_time']='-'.join(response.xpath(self.rule.datetime_xpath).extract())
        temp=response.xpath(self.rule.body_xpath).extract()
        article['body']=''.join(response.xpath(self.rule.body_xpath).extract())
        article['source_site']=self.rule.sourcesite
        article['content_type']=self.rule.urls_types
        return article



