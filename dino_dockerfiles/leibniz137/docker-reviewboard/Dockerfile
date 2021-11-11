FROM debian:wheezy
MAINTAINER ncg09@hampshire.edu

ENV DEBIAN_FRONTEND noninteractive
ENV DOMAIN localhost


RUN apt-get update \
  && apt-get install -y \
    git-core \
    libjpeg8 \
    libjpeg62-dev \
    libfreetype6 \
    libfreetype6-dev \
    patch \
    python-dev \
    python-mysqldb \
    python-pip \
    python-setuptools \
    python-subvertpy \
    memcached \
    python-imaging \
    python-svn \
    subversion \
  && easy_install reviewboard \
  && pip install -U uwsgi

COPY start.sh /
COPY uwsgi.ini /
COPY shell.sh /
RUN chmod +x /start.sh /shell.sh

EXPOSE 8000

CMD /start.sh
