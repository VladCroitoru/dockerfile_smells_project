FROM 1and1internet/ubuntu-16-apache-php-5.6:latest
MAINTAINER james.wilkins@1and1.co.uk
ARG DEBIAN_FRONTEND=noninteractive
COPY files /
RUN \
  apt-get update && \
  apt-get install -y git && \
  apt-get autoremove -y && \
  mkdir /usr/src/tmp /usr/src/tmp/zend && \
  chmod -R 777 /usr/src/tmp && \
  cd /usr/src/tmp/zend && \
  composer create-project --repository-url="https://packages.zendframework.com" zendframework/skeleton-application . 2.3.3 && \
  mv public html && \
  tar cfj /usr/src/tmp/zf2.tar.bz2 . && \
  cd .. && \
  rm -rf /usr/src/tmp/zend && \
  rm -rf /var/lib/apt/lists/* && \
  chmod -R 777 /var/www && \
  chmod -R 755 /hooks /init
