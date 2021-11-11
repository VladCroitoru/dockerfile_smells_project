# Version 0.1
FROM ubuntu:latest
MAINTAINER Scott Turnbull "scott.turnbull@us-ignite.org"

RUN apt-get update
RUN apt-get install -y make gcc ruby rubygems ruby-dev nodejs

RUN gem install jekyll rdiscount kramdown

VOLUME /jekyllsrc
EXPOSE 4000

WORKDIR /jekyllsrc
ENTRYPOINT ["jekyll"]
