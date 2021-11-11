# Pull base image.
FROM centos:centos7

ENV PHANTOMJS_VERSION 1.9.8
ENV NODE_VERION 0.10.23

# update & base packages
RUN \
  yum update -y && \
  yum -y install git gcc gcc-c++ make flex bison gperf ruby perl \
  openssl-devel freetype-devel fontconfig-devel libicu-devel sqlite-devel \
  libpng-devel libjpeg-devel bzip2 && \
  yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel readline-devel tk-devel && \
  yum install -y python-devel && \
  yum install -y curl wget


# node
RUN wget -O - http://nodejs.org/dist/v0.10.23/node-v0.10.23.tar.gz | tar xvzf - && \
    cd node-v0.10.23 && ./configure --prefix=/usr && make && make install 

# phantomjs
RUN \
  wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
  tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \
  rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
  mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /usr/local/phantomjs && \
  ln -s /usr/local/phantomjs/bin/phantomjs /usr/bin/phantomjs

RUN npm install -g grunt-cli gulp
