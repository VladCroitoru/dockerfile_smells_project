FROM ruby:latest

MAINTAINER Matt Livingston  <mylivingweb@gmail.com>

RUN echo "deb http://ftp.us.debian.org/debian wheezy-backports main" >> /etc/apt/sources.list
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y make g++ nodejs ca-certificates libmysqlclient-dev nano && \
    apt-get -y clean

RUN gem install bundle dashing puma uptimerobot faraday faraday_middleware faraday-cookie_jar dashing-contrib

RUN mkdir /dashing && \
    dashing new dashing && \
    cd /dashing && bundle && \
    ln -s /dashing/dashboards /dashboards && \
    ln -s /dashing/jobs /jobs && \
    ln -s /dashing/public /public && \
    ln -s /dashing/widgets /widgets && \
    ln -s /dashing/assets /assets && \
    mkdir /dashing/config && \
    mv /dashing/config.ru /dashing/config/config.ru && \
    ln -s /dashing/config/config.ru /dashing/config.ru && \
    ln -s /dashing/config /config

COPY run.sh /

VOLUME ["/dashboards", "/jobs", "/config", "/public", "/widgets", "/assets"]

ENV PORT 3040
EXPOSE $PORT
WORKDIR /dashing

CMD ["/run.sh"]
