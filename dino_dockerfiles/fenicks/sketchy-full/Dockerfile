# Based on Netflix docker image: https://hub.docker.com/r/netflixoss/sketchy-api/.

FROM ubuntu:14.04
MAINTAINER Christian Kakesa

ENV SKETCHY_DEV_PACKAGES python-dev libpq-dev libmysqlclient-dev libxslt-dev libxml2-dev gcc make

RUN apt-get update -y &&\
    apt-get -y -q install python-software-properties software-properties-common wget &&\
    sudo sh -c "echo 'deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main' > /etc/apt/sources.list.d/pgdg.list" &&\
    wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add - &&\
    apt-get update -y &&\
    apt-get -y -q install postgresql postgresql-contrib &&\
    apt-get -y -q install python-pip  python-psycopg2 python-virtualenv nginx supervisor git curl sudo &&\
    apt-get -y -q install libfontconfig1 build-essential &&\
    apt-get -y -q install  ${SKETCHY_DEV_PACKAGES} &&\
    wget -O /usr/local/share/phantomjs-2.1.1-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 &&\
        tar -xf /usr/local/share/phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/ &&\
        ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/phantomjs &&\
    cd /usr/local/src &&\
    git clone --depth 1 --branch master https://github.com/Netflix/sketchy.git

ENV REDIS_VERSION 3.2.1
ENV REDIS_DOWNLOAD_URL http://download.redis.io/releases/redis-3.2.1.tar.gz
ENV REDIS_DOWNLOAD_SHA1 26c0fc282369121b4e278523fce122910b65fbbf
# for redis-sentinel see: http://redis.io/topics/sentinel
RUN set -x \
	&& rm -rf /var/lib/apt/lists/* \
	&& mkdir -p /usr/local/src/redis \
	&& curl -sSL "$REDIS_DOWNLOAD_URL" -o redis.tar.gz \
	&& echo "$REDIS_DOWNLOAD_SHA1 *redis.tar.gz" | sha1sum -c - \
	&& tar -xzf redis.tar.gz -C /usr/local/src/redis --strip-components=1 \
	&& rm redis.tar.gz \
	&& make -C /usr/local/src/redis \
	&& make -C /usr/local/src/redis install \
	&& rm -r /usr/local/src/redis

# Python logger seems to have seek errors when logging to stdout in this way.
#  ln -sf /dev/stdout /usr/local/src/sketchy/sketchy-deploy.log

ADD api-start.sh /usr/local/src/sketchy/scripts/api-start.sh
ADD config-default.py /usr/local/src/sketchy/config-default.py
ADD setup.py /usr/local/src/sketchy/setup.py

RUN chmod 755 /usr/local/src/sketchy/scripts/api-start.sh

RUN cd /usr/local/src/sketchy \
    && virtualenv sketchenv \
    && . sketchenv/bin/activate \
    && python setup.py install \
    && apt-get -y -q autoremove ${SKETCHY_DEV_PACKAGES} \
    && apt-get -y -q clean \
    && apt-get -y -q autoclean

EXPOSE 8000

CMD ["/usr/local/src/sketchy/scripts/api-start.sh"]
