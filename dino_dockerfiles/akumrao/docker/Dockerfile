# MediaServer with Kafaka Dockerfile

# Base system
FROM ubuntu:18.04
RUN sed -i 's/:\/\/archive.ubuntu.com/:\/\/in.archive.ubuntu.com/g' /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y locales apt-utils curl
RUN apt-get dist-upgrade -y

# Set the locale
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get install -y build-essential cmake gcc g++ \
     git pkg-config \
     apt-transport-https \
     software-properties-common

# JDK 8
# RUN apt-get install -y default-jdk
RUN apt-get install -y openjdk-8-jdk
RUN update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java

# Bluetooth
RUN apt-get install -y bluez bluez-btsco bluez-dbg bluez-hcidump bluez-tests libbluetooth-dev libbluetooth3-dbg

# collectd
RUN apt-get install -y collectd collectd-dev collectd-utils libcollectdclient-dev

# eclipse
#RUN apt-get install -y eclipse

# gradle
#RUN apt-get install -y gradle

# jsoncpp
RUN apt-get update
RUN apt-get install -y libjsoncpp1 libjsoncpp-dev libjsoncpp-doc

# kafka libs
RUN apt-get install -y librdkafka++1 librdkafka1 librdkafka-dev kafkacat

# zookeeper
RUN apt-get install -y zookeeper zookeeperd zookeeper-bin zktop

# boost
RUN apt-get install -y libboost-all-dev

# External Sources
RUN apt-get install -y apt-transport-https

#RUN echo "deb http://www.apache.org/dist/cassandra/debian 311x main" | tee -a /etc/apt/sources.list.d/cassandra.sources.list
#RUN curl https://www.apache.org/dist/cassandra/KEYS | apt-key add -

RUN curl -fsSL https://packages.elastic.co/GPG-KEY-elasticsearch | apt-key add -
RUN echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-6.x.list

#RUN echo "deb https://packagecloud.io/grafana/stable/debian/ jessie main" | tee -a /etc/apt/sources.list.d/grafana.sources.list
#RUN curl https://packagecloud.io/gpg.key | apt-key add -

#RUN curl -sL https://repos.influxdata.com/influxdb.key | apt-key add -
#RUN echo "deb https://repos.influxdata.com/debian jessie stable" | tee /etc/apt/sources.list.d/influxdb.list

#RUN sed -i 's/:\/\/in.archive.ubuntu.com/:\/\/archive.ubuntu.com/g' /etc/apt/sources.list
RUN apt-get update

# cassandra
#RUN apt-get install -y cassandra

# Elastic Search
RUN apt-get -y install elasticsearch

# filebeat, logstash, kibana, metricbeat
RUN apt-get install -y filebeat logstash kibana metricbeat

# grafana
#RUN apt-get install -y grafana

# influxdb
#RUN apt-get install -y influxdb

# azure-iot-sdk https://github.com/Azure/azure-iot-sdk-c/blob/master/doc/ubuntu_apt-get_sample_setup.md
# FIXME: when azure-iot-sdk supports bionic use this instead
#RUN add-apt-repository ppa:aziotsdklinux/ppa-azureiot
#RUN apt-get update
#RUN apt-get install -y azure-iot-sdk-c-dev
#RUN apt-get install -y libcurl4-openssl-dev libssl-dev uuid-dev
#RUN git clone --recursive https://github.com/Azure/azure-iot-sdk-c.git
#RUN cd azure-iot-sdk-c && \
#    mkdir cmake && \
#  #  cd cmake && \
#    cmake -DCMAKE_BUILD_TYPE=Debug .. && \
#    cmake --build . -- -j2 


# BLESuite https://github.com/nccgroup/BLESuite
#RUN apt-get install -y python-dev python-pip
#RUN apt-get install -y libglib2.0-0 libglib2.0-bin libglib2.0-dev libglib2.0-dev
#RUN pip install gattlib
#RUN pip install git+https://github.com/nccgroup/BLESuite

RUN apt-get install -y unzip
# libblepp
RUN curl -L  -o libblepp-master.zip https://github.com/edrosten/libblepp/archive/master.zip
RUN unzip libblepp-master.zip && \
     cd libblepp-master && \
    ./configure && \
    make -j install

# autoconf
RUN apt-get install -y libtool automake autoconf autogen


# cppkafka
RUN apt-get install -y libssl-dev
RUN curl -L -o cppkafka-master.zip https://github.com/mfontanini/cppkafka/archive/master.zip
RUN unzip cppkafka-master.zip && \
    cd cppkafka-master && \
    mkdir build && cd build && \
    cmake .. && \
    make -j install

# rapidjson
RUN curl -o rapidjson-master.zip -L https://github.com/Tencent/rapidjson/archive/master.zip
RUN unzip rapidjson-master.zip && cd rapidjson-master && \
    mkdir build && cd build && \
    cmake .. && \
    make -j install

# kafka
RUN curl -L https://archive.apache.org/dist/kafka/1.1.1/kafka_2.11-1.1.1.tgz -o kafka_2.11-1.1.1.tgz
RUN tar xvzf kafka_2.11-1.1.1.tgz
RUN cd kafka_2.11-1.1.1 && sed -i 's/broker.id=0/broker.id=1/' config/server.properties && \
    echo "\ncontrolled.shutdown.enable=true" >> config/server.properties
RUN ln -s /kafka_2.11-1.1.1 /kafka

RUN apt-get install -y strace
RUN apt-get install -y screen rfkill
RUN apt-get update
#RUN apt-get install -y nodejs npm

#Node using NVM
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 8.10.0

RUN mkdir -p $NVM_DIR
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash \
    && . $NVM_DIR/nvm.sh \
    && nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && nvm use default

ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules
ENV PATH      $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH


# libcrc
RUN curl -L https://github.com/b2ornot2b/libcrc/archive/master.zip -o libcrc-master.zip
RUN unzip libcrc-master.zip
RUN cd libcrc-master && make

RUN apt-get update
RUN apt-get install -y net-tools sendip sudo vim gdb
RUN apt-get install -y expect
RUN apt-get install -y netcat iputils-ping

RUN apt-get install -y tcpdump

RUN apt-get install -y vim

RUN apt-get install -y ctags


RUN apt-get install -y python3-pip
RUN apt-get install -y python-pip

RUN pip install bluepy
RUN pip3 install bluepy==1.1.4
RUN npm install -g coffeescript

#installing python dependencies
RUN apt-get install -y python3-pyscard pcscd libpcsclite1 pcsc-tools
RUN pip3 install kafka-python

# Install sshpass
RUN apt-get install -y sshpass

# Install rsync
RUN apt-get install -y rsync

#Install python requests
RUN pip3 install requests

#Install SNMP Dev pkg request
RUN apt-get update
RUN apt-get install -y libsnmp-dev
RUN apt-get install -y snmp

# Cleanup
RUN apt-get clean all
RUN ldconfig -v

# Configure elasticsearch
RUN sed -i \
	-e 's/#cluster.name: my-application/cluster.name: media-doc-ES/' \
	-e 's/#bootstrap.memory_lock: true/bootstrap.memory_lock: true/g' \
	-e 's/#network.host: 192.168.0.10/http.host: 0.0.0.0/' \
	 /etc/elasticsearch/elasticsearch.yml
RUN sed -i \
	-e 's/-Xms1g/-Xms6g/' \
	-e 's/-Xmx1g/-Xmx6g/' \
	-e '$a-server' \
	/etc/elasticsearch/jvm.options

# Configure Kibana
RUN sed -i \
	-e 's/#server.host: "localhost"/server.host: "0.0.0.0"/' \
	 /etc/kibana/kibana.yml

# Configure logstash
COPY src/config/media-doc-Logstash.conf /etc/logstash/conf.d/
COPY src/config/hosts.docker /etc/hosts.docker

# set default java environment variable
# TODO: Move this to after java install 
#ENV JAVA_VERSION_MAJOR=8 \
#    JAVA_VERSION_MINOR=162 \
#    JAVA_HOME=/usr/lib/jvm/default-jvm \
#    PATH=${PATH}:/usr/lib/jvm/default-jvm/bin/

# ENV SRC=/src
# WORKDIR ${SRC}
# ADD src ${SRC}
# VOLUME src
WORKDIR /docker
