FROM ruby
MAINTAINER Andrés Espinace <saidgeek@protonmail.com>

USER root
COPY ./setup.sh /setup.sh
# install capistrano
RUN apt-get install git-core -y
RUN gem install --no-rdoc --no-ri capistrano -v 3.4.0

RUN mkdir /root/.ssh
RUN mkdir -p /source/app

WORKDIR /source/app

ENTRYPOINT ["/setup.sh"]