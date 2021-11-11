FROM ubuntu:16.04
MAINTAINER zhongpei <zhongpei@vip.qq.com>

ENV VERSION v4.20-9608-rtm-2016.04.17

RUN mkdir -p /opt/vpnclient
WORKDIR /opt/vpnclient
#RUN sed -i "s/http:\/\/archive\.ubuntu\.com/http:\/\/mirrors.163.com/" /etc/apt/sources.list
ADD requestments.txt .
ADD pap-secrets.tp /etc/ppp/pap-secrets.tp
ADD dsl-provider.tp /etc/ppp/peers/dsl-provider.tp
ADD ./endpoints /endpoints

RUN echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata && \
apt-get update -y && \
apt-get install -y -q gcc make wget python python-pip pppoe && \
apt-get install -y -q net-tools pppoeconf && \
apt-get install -y -q rsyslog && \
pip install -r requestments.txt && \
wget http://www.softether-download.com/files/softether/${VERSION}-tree/Linux/SoftEther_VPN_Client/64bit_-_Intel_x64_or_AMD64/softether-vpnclient-${VERSION}-linux-x64-64bit.tar.gz  -O /tmp/softether.tar.gz && \
tar -xzvf /tmp/softether.tar.gz -C /opt/ && \
cd /opt/vpnclient &&  make i_read_and_agree_the_license_agreement && \
mkdir -p /etc/ppp/peers/ && \
apt-get purge -y -q --auto-remove gcc make wget
ENTRYPOINT ["/usr/bin/python","/endpoints/main.py"]
