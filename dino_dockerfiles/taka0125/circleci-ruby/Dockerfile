ARG RUBY_VERSION
FROM circleci/ruby:$RUBY_VERSION

ARG BUNDLER_VERSION

RUN echo "fs.inotify.max_user_watches=204800" | sudo tee -a /etc/sysctl.conf

RUN set -x && \
    sudo apt-get update && \
    sudo apt-get install -y libldap2-dev libsasl2-dev libmariadb-dev && \
    sudo apt-get clean

RUN set -x && \
    gem update bundler && \
    gem install bundler:$BUNDLER_VERSION
