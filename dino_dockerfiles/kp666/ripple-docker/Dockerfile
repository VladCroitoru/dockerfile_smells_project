FROM ubuntu:18.04
MAINTAINER kp <dockerkp@gmail.com>


VOLUME /var/lib/rippled/db
VOLUME /opt/ripple/etc
VOLUME /var/log/rippled/

EXPOSE 5123
RUN mkdir -p /opt/ripple/bin/
RUN apt-get update; apt-get -y upgrade  &&  \
apt-get -y install git &&  \
apt-get -y install scons &&  \
apt-get -y install pkg-config &&  \
apt-get -y install protobuf-compiler &&  \ 
apt-get -y install libprotobuf-dev &&  \
apt-get -y install libssl-dev &&  \
apt-get  -y  install libboost-all-dev && \
apt-get clean

RUN git clone https://github.com/ripple/rippled.git --depth 1 -b master  &&  \
export SCONSFLAGS="-j `grep -c processor /proc/cpuinfo`" && \
cd rippled && \
scons  &&  \
build/rippled -u && \
cp -r build/rippled /opt/ripple/bin/  && \
scons -c && \
rm -rf ../rippled
CMD ["/opt/ripple/bin/rippled", "--net", "--conf", "/opt/ripple/etc/rippled.cfg"]
