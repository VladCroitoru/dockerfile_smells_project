FROM golang:1.10

MAINTAINER Matt Fellows <m@onegeek.com.au>

RUN apt-get update
RUN apt-get install -y software-properties-common curl patch gawk g++ gcc make libc6-dev patch libreadline6-dev zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool bison pkg-config libffi-dev unzip zip sudo wget
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 \
  && curl -sSL https://get.rvm.io | sudo bash -s stable

# RUN /bin/bash -l -c ". /etc/profile.d/rvm.sh && rvm install 2.2.0"
RUN /bin/bash -l -c "rvm requirements"
RUN /bin/bash -l -c "rvm install 2.2.2"
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"
RUN mkdir -p /pipeline
