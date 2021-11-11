FROM phusion/baseimage
MAINTAINER Danil Ivanov

RUN apt-get update
RUN apt-get -y install build-essential zlib1g-dev ruby-dev ruby nodejs \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/

RUN gem install github-pages -v 39

VOLUME /site
WORKDIR /site

ENTRYPOINT ["jekyll"]
