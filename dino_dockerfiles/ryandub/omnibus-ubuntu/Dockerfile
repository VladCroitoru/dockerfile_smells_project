FROM stackbrew/ubuntu:trusty
MAINTAINER ryan.walker@rackspace.com 

RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    ruby1.9.1-full \
    libssl-dev \
    libreadline-dev \
    libxslt1-dev \
    libxml2-dev \
    libcurl4-openssl-dev \
    zlib1g-dev \
    libexpat1-dev \
    libicu-dev \
    python \
    python2.7

RUN gem install bundler --no-ri --no-rdoc

RUN git config --global url."https://".insteadOf git://
RUN git config --global user.email ryan.walker@rackspace.com
RUN git config --global user.name "Ryan Walker"

RUN git clone https://github.com/ryandub/omnibus-ohai-solo.git && \
    cd omnibus-ohai-solo && \
    bundle install --binstubs

WORKDIR /omnibus-ohai-solo
