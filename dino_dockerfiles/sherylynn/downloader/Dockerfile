# Pull base image.
FROM sherylynn/wget
MAINTAINER Sherylynn <352281674@qq.com>

# 输入下载地址
ENV DOWNLOAD_URL http://pilotfiber.dl.sourceforge.net/project/lxle/Final/OS/16.04.1-64/lxle-eclectica-16.04.1.iso
ENV DOWNLOAD_PATH lxle.iso
RUN wget -q --no-check-certificate ${DOWNLOAD_URL} -O ${DOWNLOAD_PATH}
