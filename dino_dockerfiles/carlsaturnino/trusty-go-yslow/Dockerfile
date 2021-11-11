# DOCKER-VERSION 1.1.1
FROM carlsaturnino/trusty-go
MAINTAINER Carl Saturnino <cosaturn@gmail.com>

# Env
ENV PHANTOMJS_VERSION 1.9.7
ENV YSLOW_VERSION 3.1.8

RUN apt-get -qy install wget curl unzip

# PhantomJS
RUN wget --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2
RUN tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp
RUN rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2
RUN mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /opt/phantomjs
RUN ln -s /opt/phantomjs/bin/phantomjs /usr/bin/phantomjs

# YSLOW
RUN curl -k -O http://yslow.org/yslow-phantomjs-$YSLOW_VERSION.zip
RUN unzip yslow-phantomjs-$YSLOW_VERSION.zip -d yslow-phantomjs-$YSLOW_VERSION && rm yslow-phantomjs-$YSLOW_VERSION.zip
RUN mv yslow-phantomjs-$YSLOW_VERSION /opt/yslow-phantomjs-$YSLOW_VERSION
