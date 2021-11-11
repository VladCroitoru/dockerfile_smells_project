# Build a docker container to run the latest stable release of Ubiquiti's
# UniFi controller
#
# UniFi contoller is used to administer Ubiquiti wireless access points
#
#mongo 2.6
#echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen" >> /etc/apt/sources.list.d/ubiquity.list && \
#apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
#mongo 3.0
#echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse" >> /etc/apt/sources.list.d/ubiquity.list && \
#apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
#mongo 3.2
#echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" >> /etc/apt/sources.list.d/ubiquity.list && \
#apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \
#mongo 3.4
#echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" >> /etc/apt/sources.list.d/ubiquity.list && \
#apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6 && \
#mongo 3.6
#echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.6 multiverse" >> /etc/apt/sources.list.d/ubiquity.list && \
#apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 2930ADAE8CAF5059EE73BB4B58712A2291FA4AD5 && \

FROM ubuntu:xenial
MAINTAINER dmreiland@unixsherpa.com

ENV DEBIAN_FRONTEND noninteractive

RUN mkdir -p /usr/lib/unifi/data && \
  	touch /usr/lib/unifi/data/.unifidatadir && \
    apt-get update -q -y && \
    apt-get install -q -y apt-transport-https && \
    apt-get install -q -y apt-utils lsb-release curl wget rsync software-properties-common python-software-properties java-common && \
    echo "deb http://www.ubnt.com/downloads/unifi/debian stable ubiquiti" > /etc/apt/sources.list.d/ubiquity.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 06E85760C0A52C50 && \
    echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" >> /etc/apt/sources.list.d/ubiquity.list && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6 && \
    wget -O /tmp/amazon-corretto.deb https://d3pxv6yz143wms.cloudfront.net/8.212.04.1/java-1.8.0-amazon-corretto-jdk_8.212.04-1_amd64.deb && \
    dpkg --install /tmp/amazon-corretto.deb && \
    rm -f /tmp/amazon-corretto.deb && \
    apt-get update -q -y && \
    apt-get install -q -y mongodb-org && \
    apt-get install -q -y unifi && \
    rm -rf /var/lib/apt/lists/* && \
    mv /usr/bin/mongod /usr/bin/mongod.bin

COPY scripts/init.sh /usr/local/bin/init.sh
COPY scripts/mongod /usr/bin/mongod.sh
COPY scripts/mongod.conf /etc/mongod.conf

VOLUME /usr/lib/unifi/data
EXPOSE  8443/tcp 8080/tcp 27117/tcp 3478/udp 8883/tcp 6789/tcp
WORKDIR /usr/lib/unifi
ENTRYPOINT ["/bin/bash", "/usr/local/bin/init.sh"]
