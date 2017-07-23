INSERT INTO articlerule(NAME,domains,start_urls,urls_types,nextpage_xpath,articleurl_xpath,body_xpath,title_xpath,datetime_xpath,sourcesite,filter_xpath,filter_regex,minvalue,ENABLE)
VALUES('博客园','cnblogs.com','https://www.cnblogs.com/cate/java/','1','//div[@class="pager"]/a[last()]/@href','//div[@class="post_item_body"]/h3/a/@href','//div[@id="cnblogs_post_body"]/text()','//a[@id="cb_post_title_url"]/text()','//span[@id="post-date"]/text()','博客园','//span[@class="article_view"]/a/text()','阅读\\((\\d+)\\)',200,1);

INSERT INTO articlerule(NAME,domains,start_urls,urls_types,nextpage_xpath,articleurl_xpath,body_xpath,title_xpath,datetime_xpath,sourcesite,filter_xpath,filter_regex,minvalue,ENABLE)
VALUES('并发编程网','ifeve.com','http://ifeve.com/category/java/','1','//a[@class="next page-numbers"]/@href','//div[@class="post"]/h3/a/@href','//div[@class="post_content"]/text()','//h3[@class="title"]/span/text()','//li[@class="post_date clearfix"]/span/text()','并发编程网Java社区','//li[@class="post_comment"]/text()','\\r\\n(\\d+),?',3000,1)

SELECT * FROM articlerule;

DELETE FROM articlerule;

DROP TABLE articlerule;

CREATE TABLE articlerule(
	id INT PRIMARY KEY AUTO_INCREMENT,
	NAME VARCHAR(30),
	domains VARCHAR(100),
	start_urls VARCHAR(200),
	urls_types VARCHAR(30),
	nextpage_xpath VARCHAR(100),
	articleurl_xpath VARCHAR(100),
	body_xpath VARCHAR(100),
	title_xpath VARCHAR(100),
	datetime_xpath VARCHAR(100),
	sourcesite VARCHAR(100),
	filter_xpath VARCHAR(100),
	filter_regex VARCHAR(100),
	minvalue INT,
	ENABLE INT
);

INSERT INTO articletype(NAME) VALUES('Python');

SELECT * FROM articletype;

SELECT * FROM article;

DELETE FROM article;

DROP TABLE article;

CREATE TABLE article(
	id INT PRIMARY KEY AUTO_INCREMENT,
	title VARCHAR(100),
	content TEXT,
	contenttype INT,
	posttime VARCHAR(30),
	originurl VARCHAR(100),
	sourcesite VARCHAR(100)
);

SELECT * FROM article WHERE title LIKE '%WebSocket%';