# -*- coding: utf-8 -*-
import scrapy


class XzxzdSpider(scrapy.Spider):
    name = 'xzxzd'
    allowed_domains = ['qidian.com']
    start_urls = ['https://book.qidian.com/info/1010734492']

    def parse(self, response):
    	pages = response.xpath('//div[@id="j-catalogWrap"]//ul[@class="cf"]/li')
    	a = 0
    	for page in pages:
    		a = a + 1 
    		url = page.xpath('./child::a/attribute::href').extract_first()
    		idx = page.xpath('./attribute::data-rid').extract_first()
    																	# //*[@id="j-catalogWrap"]/div[2]/div[1]/h3/text()[1]
    		# uri_name = page.xpath('../..//h3/text()[1]').extract() ######not working
    		uri_name = page.xpath('../..//h3/text()[2]').extract()[0].strip() ######not working
    		# chap_name.write(uri_name.encode('utf-8'))
    		print uri_name
    		req = response.follow(url, callback= self.parse_chapter)
    		req.meta['idx'] = idx
    		req.meta['uri_name'] = uri_name
    		yield req
    		if a == 4:
    			break
    	pass
    def parse_chapter(self,response):
    	uri_name = response.meta['uri_name']
    	idx = response.meta['idx']
    	title = response.xpath('//div[@class="main-text-wrap"]//h3[@class="j_chapterName"]/text()').extract_first().strip()
    	content = response.xpath('//div[@class="main-text-wrap"]//div[@class="read-content j_readContent"]').extract_first().strip()

    	filename = './down/%s_%s_%s.text' % (uri_name,idx,title)
    	cnt = '<h1>%s</h1> %s' % (title,content)
    	with open(filename,'wb') as f:
    		f.write(cnt.encode('utf-8'))
    	# print filename
    	# print idx
    	# print title
    	# print content
    	pass