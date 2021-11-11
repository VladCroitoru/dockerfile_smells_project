# Selenium + Firefox

FROM alpine:3.4
MAINTAINER leafney "babycoolzx@126.com"

# 更新软件源
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.4/main" >> /etc/apk/repositories && \
	echo "http://dl-4.alpinelinux.org/alpine/v3.4/community" >> /etc/apk/repositories


RUN apk update && \
	apk add python py-pip curl unzip dbus-x11 ttf-freefont firefox-esr xvfb && \
	pip install selenium && \
	pip install pyvirtualdisplay

# 从网上下载 geckodriver
#RUN curl https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz -O && \
#	tar -zxvf geckodriver-v0.11.1-linux64.tar.gz && \
#	mv ./geckodriver /usr/local/bin/ && \
#	chmod a+x /usr/local/bin/geckodriver

# 拷贝本地的 geckodriver
 COPY ./geckodriver /usr/local/bin/
 RUN chmod a+x /usr/local/bin/geckodriver
