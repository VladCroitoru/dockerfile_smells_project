FROM ubuntu:14.04
MAINTAINER Joseph Scavone
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update ;\
    apt-get install -y software-properties-common ;\
    add-apt-repository ppa:brightbox/ruby-ng ;\
    apt-get update ;\
    apt-get install -y tar python-software-properties build-essential curl libreadline-dev libcurl4-gnutls-dev libpq-dev libxml2-dev libxslt1-dev zlib1g-dev libssl-dev git-core ruby2.6 ruby2.6-dev libgmp3-dev ;\
    apt-get clean

RUN \
    cd /opt ;\
    git clone https://github.com/feedbin/refresher.git ;\
    cd refresher ;\
    gem install bundler redis

RUN \
    cd /opt/refresher ;\
    bundle

ADD startup.sh /feedbin-start

CMD ["/bin/bash", "/feedbin-start"]
