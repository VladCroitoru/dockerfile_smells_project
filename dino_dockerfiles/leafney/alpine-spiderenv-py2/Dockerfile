FROM alpine:3.5
MAINTAINER leafney "babycoolzx@126.com"

# 更新软件源
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.5/main" > /etc/apk/repositories && \
	echo "http://dl-4.alpinelinux.org/alpine/v3.5/community" >> /etc/apk/repositories

# 安装相关软件
# 基础依赖: python pip curl 解压 sqlite3数据库
# 安装 firefox 相关依赖包及 firefox 程序
# 安装 chrome 相关依赖包及 chrome 程序和 driver
# 安装显示框架 pyvirtualdisplay 和 xvfb 用于无GUI情况下显示网页
# 安装 lxml 和 beautifulsoup4 网页解析库
# 安装 requests 请求库
# 安装 xmltodict 工具库
# 安装 Scrapy 爬虫库(about 200MB)
# 安装 selenium 自动化测试工具
# 安装 apscheduler 用于启用定时任务
# 安装 supervisor 进程管理工具
# 安装glances 资源监控工具 

RUN apk update && \
	apk add python python-dev py2-pip py-lxml curl unzip sqlite && \
	apk add xvfb py2-psutil && \
	apk add gcc musl-dev libgcc openssl-dev libxml2-dev libxslt-dev libffi-dev libxml2 libxslt && \
	mkdir -p /etc/supervisor/conf.d && \
	mkdir -p /app

# install firefox and chrome
RUN	apk add dbus-x11 ttf-freefont firefox-esr && \
	apk add libexif udev chromium chromium-chromedriver

COPY ./requirements.txt /
RUN pip install -r requirements.txt

# 设置时区
RUN apk add ca-certificates && \
	apk add tzdata && \
	ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
	echo "Asia/Shanghai" > /etc/timezone

RUN rm -rf /var/cache/apk/*

# 安装 geckodriver

# 方法一: 从Github下载安装: https://github.com/mozilla/geckodriver/releases

# ENV GECKODRIVER_VERSION v0.13.0

# RUN curl https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz -O && \
# 	tar -zxvf geckodriver-$GECKODRIVER_VERSION-linux64.tar.gz && \
# 	mv ./geckodriver /usr/local/bin/ && \
# 	chmod a+x /usr/local/bin/geckodriver


# 方法二: 由于网络原因无法下载geckodriver, 拷贝本地geckodriver(v0.13.0)

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

# port for supervisor and glances
EXPOSE 9001 61208

CMD ["supervisord", "--nodaemon", "--configuration", "/etc/supervisor/supervisord.conf"]