FROM debian:stretch

MAINTAINER Emmanuel Vanhoucke <emmanuel.vanhoucke@a-sis.com>

RUN apt-get update && apt-get install -y ruby bundler nodejs git curl linux-perf procps cmake g++ sudo unzip vim wget && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN cd /usr/share && \
    wget https://github.com/Icinga/dashing-icinga2/archive/master.zip && \
    unzip master.zip && \
    mv dashing-icinga2-master /dashing && \
    cd /dashing

RUN gem install bundler dashing

RUN cd /dashing && \
    bundle install

VOLUME ["/dashboards", "/jobs", "/lib-dashing", "/config", "/public", "/widgets", "/assets"]

ENV PORT 3030
EXPOSE $PORT
WORKDIR /dashing

CMD ["/dashing/run.sh"]
