FROM ubuntu:12.04
MAINTAINER Liftopia Operations ops@liftopia.com

RUN \
  apt-get update ;\
  apt-get -y install python-software-properties wget openssl libreadline6 libreadline6-dev curl git zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf libc6-dev ncurses-dev automake libtool bison subversion zlib1g-dev build-essential libreadline-dev libsqlite3-dev libxml2-dev libxslt1-dev ;\
  curl -L get.rvm.io | bash -s stable ;\
  useradd -m docker -s /bin/bash

ENV PATH /usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

CMD [ "/bin/bash", "--login" ]
