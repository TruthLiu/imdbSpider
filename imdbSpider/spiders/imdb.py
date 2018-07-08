# -*- coding: utf-8 -*-
import scrapy
import os
from urllib import parse


from scrapy import Request


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    allowed_domains = ['www.imdb.com']
    start_urls = ['http://www.imdb.com/']

    def parse(self, response):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/result/"
        # we have 39 document
        for i in range(107):
            with open(path+str(i)+".txt","r") as f:
                for line in f.readlines():
                    line=line.rstrip('\n')
                    url=response.url+"find?"+line
                    yield Request(url=url,callback=self.parse1)


    def parse1(self,response):
        url=response.css(".findList tr td.result_text a::attr(href)").extract()
        if len(url)==0:
            print("not search the moive!")
        else:
            url_new=parse.urljoin(response.url,url[0])
            yield Request(url=url_new,callback=self.parse_detail)


    def parse_detail(self,response):
        plot=response.css(".inline.canwrap p span::text").extract()
        if len(plot)==0:
            print("该电影无plot")
        else:
            path_plot=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/plot/'
            if not os.path.exists(path_plot):
                os.mkdir(path_plot)
            with open(path_plot+'10m_plot.txt','a') as f:
                f.writelines(plot[0]+"\n")
                f.close()