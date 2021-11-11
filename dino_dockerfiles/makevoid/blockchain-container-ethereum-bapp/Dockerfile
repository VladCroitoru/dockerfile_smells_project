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
#
# parity 1.4.5
# RUN wget http://d1h4xl4cr1h0mo.cloudfront.net/v1.4.5/x86_64-unknown-linux-gnu/parity_1.4.5_amd64.deb && dpkg -i parity_1.4.5_amd64.deb
#
# parity 1.3.8
# RUN wget https://github.com/ethcore/parity/releases/download/v1.3.8/parity_1.3.8-0_amd64.deb && dpkg -i parity_1.3.8-0_amd64.deb
#
# parity 1.3.14 
RUN wget http://d1h4xl4cr1h0mo.cloudfront.net/v1.3.14/x86_64-unknown-linux-gnu/parity_1.3.14_amd64.deb && dpkg -i parity_1.3.14_amd64.deb
#



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


# ---------------------------------------------------------------------

# from here we define some custom initialization for the current staging version of Bapp which uses mysql2 for caching and initial data validation



#
# # run APT installs before anything else
# #
# # note: for nokogiri - TODO recheck - probably only libxml2-dev is needed
RUN apt install ruby-dev libxml2-dev zlib1g-dev liblzma-dev libxslt-dev net-tools libmysqlclient-dev -y
# TODO: publish makevoid/blockchain-container2 including these apt installs



# TODO: recheck why this is failing to set the password
#
# TODO: find a way to reconfigure the root mysql password via prompt
#
# RUN echo "mysql-server-5.7 mysql-server/root_password foo root" | debconf-set-selections
# RUN echo "mysql-server-5.7 mysql-server/root_password_again foo root" | debconf-set-selections
RUN apt -y install mysql-server


# RUN echo `/usr/sbin/mysqld`
RUN test -e /var/run/mysqld || install -m 755 -o mysql -g root -d /var/run/mysqld

# no password
#
RUN su - mysql -s /bin/sh -c "/usr/bin/mysqld_safe &" && sleep 3 && mysql -u root -e "CREATE DATABASE bapp;"





# CMD /www/app/docker/set_container_id                && \
    # cd /www/app/parity                              && \
    # pm2 start --interpreter bash -n parity ./run    && \


# set_container_id script:
#
# #!/usr/bin/env bash
# echo `ifconfig eth0 | grep -oP 'inet addr:\d+\.\d+\.\d+\.\K\d+'` > /tmp/container_id


# temporary command (bash shell) - note that this image should be ran as a base image dependency (include "FROM makevoid/blockchain-container-ethereum-bapp" in your Dockerfile)
CMD bash
