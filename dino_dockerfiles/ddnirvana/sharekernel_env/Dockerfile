FROM ubuntu:15.04
MAINTAINER Ddnirvana "ddnirvana1@gmail.com"

RUN apt-get -qq update && apt-get install -y curl vim git build-essential net-tools iputils-ping pciutils iperf iperf3 openssh-server wget module-init-tools ethtool nginx; 

COPY iperf_test.sh /home/iperf_test.sh
COPY iperf_server.sh /home/iperf_server.sh
COPY iperf_server_nm.sh /home/iperf_server_nm.sh
COPY build_net.sh /home/build_net.sh
COPY modules /home/modules
COPY bin /home/bin

#$VOLUME ["/root"]
WORKDIR /home
