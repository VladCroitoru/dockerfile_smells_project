FROM centos:latest

MAINTAINER Lair Junior

RUN yum install -y wget
RUN yum install -y openssl

RUN wget https://cli-assets.heroku.com/branches/stable/heroku-linux-amd64.tar.gz -O heroku.tar.gz \
 && mkdir -p /usr/local/lib \
 && tar -xvzf heroku.tar.gz -C /usr/local/lib \
 && /usr/local/lib/heroku/install

RUN yum update -y
RUN yum groupinstall -y "Development Tools"

RUN yum install -y gcc-c++ patch readline readline-devel zlib zlib-devel \
 && yum install -y libyaml-devel libffi-devel openssl-devel make \
 && yum install -y bzip2 autoconf automake libtool bison iconv-devel which

RUN gpg2 --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 \
 && curl -L get.rvm.io | bash -s stable \
 && source /etc/profile.d/rvm.sh

RUN /bin/bash -l -c "rvm install 1.9.3 && rvm use 1.9.3 --default"
RUN /bin/bash -l -c "gem update --system"
RUN /bin/bash -l -c "gem install travis -v 1.8.8 --no-rdoc --no-ri"
