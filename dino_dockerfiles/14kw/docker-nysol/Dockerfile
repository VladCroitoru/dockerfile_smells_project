FROM ubuntu:precise

RUN apt-get update
RUN apt-get install -y g++ build-essential autotools-dev autoconf libtool libxml2 libxml2-dev libiconv* libicu-dev libbz2-dev python-dev ruby1.9.3 sudo libboost-all-dev
ADD nysol_2.4-0_amd64.deb /usr/local/src
RUN cd /usr/local/src && dpkg -i nysol_2.4-0_amd64.deb
