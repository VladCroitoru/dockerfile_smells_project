FROM ubuntu:16.04
MAINTAINER leafney "babycoolzx@126.com"

RUN echo "deb http://cn.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse" >> /etc/apt/sources.list && \
	echo "deb http://cn.archive.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse" >> /etc/apt/sources.list && \
	echo "deb http://cn.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse" >> /etc/apt/sources.list

# 安装相关软件
# 基础依赖: python pip curl 解压 sqlite3数据库
# 安装 phantomjs
# 安装 firefox 相关依赖包及 firefox 程序
# 安装 chrome 相关依赖包及 chrome 程序和 driver
# 安装显示框架 pyvirtualdisplay 和 xvfb 用于无GUI情况下显示网页
# 安装 lxml 和 beautifulsoup4 网页解析库
# 安装 requests 请求库
# 安装 xmltodict 工具库
# 安装 Scrapy 爬虫库
# 安装 selenium 自动化测试工具
# 安装 apscheduler 用于启用定时任务
# 安装 supervisor 进程管理工具
# 安装glances 资源监控工具 

RUN apt-get update

RUN apt-get -y install python python-dev python-pip curl unzip sqlite3 && \
	apt-get -y install libxml2-dev libxslt1-dev zlib1g-dev && \
	mkdir -p /etc/supervisor/conf.d && \
	mkdir -p /app

RUN pip install --upgrade pip && \
	pip install lxml && \
	pip install beautifulsoup4 && \
	pip install xmltodict && \
	pip install apscheduler && \
	pip install supervisor && \
	pip install glances && \
	pip install docker-py && \
	pip install pystache && \
	pip install bottle

# Setting timezone
RUN ln -sf /usr/share/zoneinfo/Asia/ShangHai /etc/localtime && \
	echo "Asia/Shanghai" > /etc/timezone && \
	dpkg-reconfigure -f noninteractive tzdata

# Install phantomjs

# 方法一 从官网下载 phantomjs并安装
# https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2

# ENV PHANTOMJS_VERSION 2.1.1

# RUN set -x && \
# 	cd /tmp/ && \
# 	export PHANTOMJS="phantomjs-$PHANTOMJS_VERSION-linux-x86_64" && \
# 	curl https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOMJS.tar.bz2 -O && \
# 	tar xvjf $PHANTOMJS.tar.bz2 && \
# 	mv $PHANTOMJS /usr/local/share && \
# 	ln -sf /usr/local/share/$PHANTOMJS/bin/phantomjs /usr/local/bin && \
# 	rm -rf *

# 方法二 由于网络原因无法下载，拷贝本地 phantomjs-2.1.1-linux-x86_64.tar.bz2(v2.1.1)

COPY ./phantomjs-2.1.1-linux-x86_64.tar.bz2 /tmp/
RUN set -x && \
	cd /tmp/ && \
	export PHANTOMJS="phantomjs-2.1.1-linux-x86_64" && \
	tar xvjf $PHANTOMJS.tar.bz2 && \
	mv $PHANTOMJS /usr/local/share && \
	ln -sf /usr/local/share/$PHANTOMJS/bin/phantomjs /usr/local/bin && \
	rm -rf *

# 安装 geckodriver

# 方法一: 从Github下载安装: https://github.com/mozilla/geckodriver/releases

# ENV GECKODRIVER_VERSION v0.13.0

# RUN curl https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -O && \
# 	tar -zxvf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
# 	mv ./geckodriver /usr/local/bin/ && \
# 	chmod a+x /usr/local/bin/geckodriver

# 方法二: 由于网络原因无法下载geckodriver, 拷贝本地geckodriver(v0.13.0)
# copy local geckodriver file

COPY ./geckodriver /usr/local/bin/
RUN chmod a+x /usr/local/bin/geckodriver

# setting supervisor and glances config
COPY ./supervisord.conf /etc/supervisor/supervisord.conf
COPY ./glances.conf /etc/supervisor/conf.d/glances.conf

COPY ./docker-entrypoint.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
RUN chmod +x usr/local/bin/docker-entrypoint.sh
ENTRYPOINT ["docker-entrypoint.sh"]

WORKDIR /app
VOLUME ["/app"]
USER root

# port for supervisor and glances
EXPOSE 9001 61208

CMD ["supervisord", "--nodaemon", "--configuration", "/etc/supervisor/supervisord.conf"]