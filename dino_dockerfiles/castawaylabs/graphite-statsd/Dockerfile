FROM ubuntu:trusty
MAINTAINER Matej Kramny <matejkramny@gmail.com>

# Inspired from https://github.com/hopsoft/docker-graphite-statsd

RUN echo deb http://archive.ubuntu.com/ubuntu $(lsb_release -cs) main universe > /etc/apt/sources.list.d/universe.list
RUN apt-get -y update

# Install dependencies
RUN apt-get -y --force-yes install vim \
  nginx \
  python-flup \
  expect \
  git \
  memcached \
  sqlite3 \
  libcairo2 \
  libcairo2-dev \
  python-cairo \
  pkg-config \
  wget \
  python-dev \
  supervisor \
  openssl \
  nodejs

# Configure log dirs (might be useless)
RUN mkdir -p /var/log/nginx
RUN mkdir -p /var/log/carbon
RUN mkdir -p /var/log/graphite

ADD conf/distribute_setup.py /opt/distribute_setup.py
RUN python /opt/distribute_setup.py
RUN easy_install pip

RUN pip install django==1.3
RUN pip install python-memcached==1.53
RUN pip install django-tagging==0.3.1
RUN pip install whisper==0.9.12
RUN pip install twisted==11.1.0
RUN pip install txAMQP==0.6.2

# get source code
RUN git clone -b 0.9.12 https://github.com/graphite-project/graphite-web.git /usr/local/src/graphite-web
RUN git clone -b 0.9.12 https://github.com/graphite-project/whisper.git /usr/local/src/whisper
RUN git clone -b 0.9.12 https://github.com/graphite-project/carbon.git /usr/local/src/carbon
RUN git clone -b v0.7.2 https://github.com/etsy/statsd.git /opt/statsd

# Install Graphite
WORKDIR /usr/local/src/graphite-web
RUN python ./setup.py install

# Install Whisper
WORKDIR /usr/local/src/whisper
RUN python ./setup.py install

# Install Carbon
WORKDIR /usr/local/src/carbon
RUN python ./setup.py install

# Configure nginx site
RUN rm -rf /etc/nginx/sites-enabled/*

ADD conf/nginx.conf /etc/nginx/sites-enabled/graphite
ADD conf/graphite_syncdb.sh /opt/graphite_syncdb
ADD conf/supervisord.conf /etc/supervisord.conf

# Graphite/statsd/carbon config files
ADD conf/statsd-config.js /opt/statsd/config.js
ADD conf/aggregation-rules.conf /opt/graphite/conf/aggragation-rules.conf
ADD conf/blacklist.conf /opt/graphite/conf/blacklist.conf
ADD conf/carbon.amqp.conf /opt/graphite/conf/carbon.amqp.conf
ADD conf/carbon.conf /opt/graphite/conf/carbon.conf
ADD conf/relay-rules.conf /opt/graphite/conf/relay-rules.conf
ADD conf/rewrite-rules.conf /opt/graphite/conf/rewrite-rules.conf
ADD conf/storage-aggregation.conf /opt/graphite/conf/storage-aggregation.conf
ADD conf/storage-schemas.conf /opt/graphite/conf/storage-schemas.conf
ADD conf/whitelist.conf /opt/graphite/conf/whitelist.conf
ADD conf/local_settings.py /opt/graphite/webapp/graphite/local_settings.py

# Configure django DB
RUN chmod 775 /opt/graphite_syncdb
RUN /opt/graphite_syncdb

# Expose common ports
EXPOSE 80
EXPOSE 2003
EXPOSE 8125/udp

# Enable users of this container to mount their volumes (optional)
VOLUME /var/log
VOLUME /opt/graphite/storage
VOLUME /opt/graphite/conf

# Start supervisor by default
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
