##
# Gitlab CI Runner with NodeJS MongoDB Redis
#
# This creates an image which contains an Gitlab CI Runner environment
# for NodeJS app ecosystem
# - Node.js 0.10.23
# - MongoDB 2.4.8
# - Redis 2.4.15
# - Git
##

FROM truongsinh/nodejs-mongodb-redis

MAINTAINER TruongSinh Tran-Nguyen <i@truongsinh.pro>

# Config
ENV INSTALL_RUBY_VERSION 2.0.0-p247

ENV HOME /root

WORKDIR /root

# apt-get build deps, to be removed later
RUN apt-get -y update \
 && apt-get -y install build-essential wget unzip libssl-dev

# This is neccesary at runtime.
RUN apt-get -y install openssh-client git libicu-dev

# install ruby, bundler, and clean up
RUN wget http://cache.ruby-lang.org/pub/ruby/2.0/ruby-2.0.0-p353.tar.gz \
 && tar -xvzf ruby-2.0.0-p353.tar.gz \
 && cd ruby-2.0.0-p353/ \
 && ./configure --prefix=/usr/local --disable-install-rdoc \
 && make && make install \
 && cd .. \
 && rm -rf ruby-2.0.0-p353*


# install gitlab-ci-runner

RUN wget --no-check-certificate https://github.com/gitlabhq/gitlab-ci-runner/archive/master.zip \
 && unzip master.zip \
 && rm -rf master.zip \
 && cd gitlab-ci-runner-master \
 && gem install bundler \
 && bundle install

# prepare SSH
RUN mkdir -p /root/.ssh

# Clean up
RUN apt-get -y purge build-essential wget unzip libssl-dev \
 && apt-get -y autoremove

# Start MongoDB, Redis and Runner
CMD mongod --fork -f /etc/mongodb.conf \
 && redis-server /etc/redis/redis.conf \
 && cd $HOME/gitlab-ci-runner-master && ssh-keyscan -H $GITLAB_SERVER_FQDN >> $HOME/.ssh/known_hosts && bundle exec ./bin/setup_and_run


