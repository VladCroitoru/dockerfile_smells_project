FROM debian:jessie

# GENERAL DEPENDENCIES

RUN apt-get update && \
    apt-get -y install curl

# JAVA
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" | tee -a /etc/apt/sources.list.d/jessie-backports.list
RUN apt-get update
RUN apt-get -y install openjdk-8-jdk

# Pip
RUN apt-get -y install python-pip

# Memcached
#RUN apt-get update
RUN apt-get -y install memcached
RUN pip install python-memcached
RUN pip install gunicorn

# Redis
#RUN apt-get update
RUN apt-get -y install build-essential
RUN apt-get -y install tcl8.5
RUN curl -sL --retry 3 http://download.redis.io/releases/redis-stable.tar.gz > redis-stable.tar.gz
RUN tar xzf redis-stable.tar.gz && cd redis-stable/ && make
#RUN pwd 
RUN cd redis-stable && make test
RUN cd redis-stable && make install 
RUN cd redis-stable && cd utils && ./install_server.sh

# CF_RECOMMENDER
RUN pip install cf_recommender

# Flask
RUN apt-get -y install python-dev
RUN pip install Flask

# Cron
RUN apt-get -y install cron
ADD docker/crontab /app/crontab
RUN crontab /app/crontab

# Project env and files
ENV PROJECT_HOME /Preco
RUN mkdir /Preco
RUN mkdir /Preco/src
RUN mkdir /Preco/data
COPY src /Preco/src/
COPY data /Preco/data/
COPY README.md /Preco/
#RUN ls /Preco
RUN chmod u+x /Preco/src/main/script/autostart.sh

ENTRYPOINT ["/Preco/src/main/script/autostart.sh"]

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="mlaas-cfreco-mini" \
      org.label-schema.description="Fast in memory item-item recommendation engine" \
      org.label-schema.url="http://kolibero.eu" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/goliasz/mlaas-cfreco-mini" \
      org.label-schema.vendor="KOLIBERO" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"
