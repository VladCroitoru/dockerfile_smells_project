FROM ubuntu:15.10

RUN export TERM=dumb ; export DEBIAN_FRONTEND=noninteractive ; apt-get update && apt-get install -y \
  curl \
  git=1:2.5.0-1ubuntu0.2 \
  openjdk-8-jdk=8u91-b14-3ubuntu1~15.10.1 \
  python=2.7.9-1 \
  python3=3.4.3-4ubuntu1 \
  php5=5.6.11+dfsg-1ubuntu3.4 \
  php5-curl=5.6.11+dfsg-1ubuntu3.4 \
  php5-gd=5.6.11+dfsg-1ubuntu3.4 \
  php5-imagick=3.3.0~rc2-1 \
  php5-imap=5.4.6-0ubuntu6 \
  php5-intl=5.6.11+dfsg-1ubuntu3.4 \
  php5-mcrypt=5.4.6-0ubuntu6 \
  php5-memcache=3.0.8-5build1 \
  php5-memcached=2.2.0-2build1 \
  php5-ming=1:0.4.5-1.2ubuntu2 \
  php5-mysql=5.6.11+dfsg-1ubuntu3.4 \
  php5-pgsql=5.6.11+dfsg-1ubuntu3.4 \
  php5-ps=1.3.7-1ubuntu2 \
  php5-pspell=5.6.11+dfsg-1ubuntu3.4 \
  php5-recode=5.6.11+dfsg-1ubuntu3.4 \
  php5-sqlite=5.6.11+dfsg-1ubuntu3.4 \
  php5-tidy=5.6.11+dfsg-1ubuntu3.4 \
  php5-xcache=3.2.0-1build1 \
  php5-xmlrpc=5.6.11+dfsg-1ubuntu3.4 \
  php5-xsl=5.6.11+dfsg-1ubuntu3.4 \
  haproxy=1.5.14-1ubuntu0.15.10.1 \
  msmtp=1.6.2-1 \
  supervisor=3.0r1-1 \
  wget \
  && apt-get clean && rm -rf /var/lib/apt/lists/*

CMD /bin/bash
