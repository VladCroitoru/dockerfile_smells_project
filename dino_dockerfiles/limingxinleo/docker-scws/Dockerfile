# scws docker
# created by limingxinleo
#
# START COMMAND:

# docker run --rm -it limingxinleo/docker-scws /usr/local/scws/bin/scws -h
#

FROM ubuntu:14.04
MAINTAINER limx <715557344@qq.com>

# 更新依赖
RUN apt-get update -qq
RUN apt-get install -qy --no-install-recommends \
	wget make gcc g++ bzip2 zlib1g-dev 

# 安装scws
RUN wget http://www.xunsearch.com/scws/down/scws-1.2.3.tar.bz2 && \
	tar xvjf scws-1.2.3.tar.bz2 && \
	cd scws-1.2.3 && \
	./configure --prefix=/usr/local/scws && \
	make && \
	make install

RUN ls -al /usr/local/scws/lib/libscws.la && \
	/usr/local/scws/bin/scws -h

# 推送分词PHP扩展到/usr/local/scws/ext
# RUN cp -r phpext /usr/local/scws/

#下载分词字典
RUN cd /usr/local/scws/etc && \
	wget http://www.xunsearch.com/scws/down/scws-dict-chs-gbk.tar.bz2 && \
	wget http://www.xunsearch.com/scws/down/scws-dict-chs-utf8.tar.bz2 && \
	tar xvjf scws-dict-chs-gbk.tar.bz2 && \
	tar xvjf scws-dict-chs-utf8.tar.bz2



