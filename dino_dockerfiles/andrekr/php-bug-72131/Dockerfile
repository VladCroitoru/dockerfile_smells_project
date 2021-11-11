FROM ubuntu:14.04

ENV php_version 5.5

RUN apt-get update
RUN apt-get -y upgrade
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install golang software-properties-common
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install php${php_version}-cli php${php_version}-curl

COPY server/server.go /root/server/
COPY test.php /root/
RUN cd /root/server/ ; go build

CMD php --version ; /root/server/server & php /root/test.php
