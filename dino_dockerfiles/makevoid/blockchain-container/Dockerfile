FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

# solc and geth (geth is used just to run attach)
RUN apt-get update      -y --ignore-missing              && \
    apt-get install     -y software-properties-common apt-utils wget  && \
    add-apt-repository  -y ppa:ethereum/ethereum                      && \
    add-apt-repository  -y ppa:ethereum/ethereum-dev                  && \
    apt-get             -y update                                     && \
    apt-get install     -y solc geth

# TODO: run apt clean

# parity
#
RUN wget https://github.com/ethcore/parity/releases/download/v1.3.8/parity_1.3.8-0_amd64.deb && dpkg -i parity_1.3.8-0_amd64.deb

RUN apt-get install -y python curl git unzip

# node 6 from package
#
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

RUN npm i -g coffee-script pm2


# ruby from package
#
RUN apt-get install software-properties-common && \
    apt-add-repository ppa:brightbox/ruby-ng && \
    apt-get update && \
    apt-get install ruby2.3 -y  && \
    gem i bundler


# build-essential not always needed (just if your lib has C dependencies)
RUN apt-get install -y build-essential ruby2.3-dev  libsqlite3-dev



# CMD /www/app/docker/set_container_id                && \
    # cd /www/app/parity                              && \
    # pm2 start --interpreter bash -n parity ./run    && \


# set_container_id script:
#
# #!/usr/bin/env bash
# echo `ifconfig eth0 | grep -oP 'inet addr:\d+\.\d+\.\d+\.\K\d+'` > /tmp/container_id


