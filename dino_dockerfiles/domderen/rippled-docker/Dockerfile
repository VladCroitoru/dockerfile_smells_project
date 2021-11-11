FROM ubuntu:14.04

# hopefully temporary work-around of http://git.io/Ke_Meg#1724 
RUN apt-mark hold initscripts udev plymouth mountall

# Add package sources
RUN apt-get -y update
RUN apt-get -y install software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test


RUN apt-get -y update
RUN apt-get -y upgrade


# Various dependencies
RUN apt-get -y install pkg-config
RUN apt-get -y install git
RUN apt-get -y install scons
RUN apt-get -y install ctags


RUN add-apt-repository ppa:boost-latest/ppa
RUN apt-get -y install libboost1.55-all-dev


RUN apt-get -y install protobuf-compiler
RUN apt-get -y install libprotobuf-dev
RUN apt-get -y install libssl-dev

# Upgrade to gcc-4.9 (after some other package pulls in gcc)
RUN apt-get -y install gcc-4.9 g++-4.9
RUN rm -f /usr/bin/gcc && ln -s /usr/bin/gcc-4.9 /usr/bin/gcc
RUN rm -f /usr/bin/g++ && ln -s /usr/bin/g++-4.9 /usr/bin/g++


# Checkout the ripple source
RUN git clone https://github.com/ripple/rippled.git /opt/rippled -b develop
RUN cd /opt/rippled && scons build/rippled


# peer_port
EXPOSE 51235
# websocket_public_port
EXPOSE 5006
# websocket_port (trusted access)
EXPOSE 6006


# Share the ripple data directory
VOLUME /var/lib/rippled

RUN mkdir /opt/rippled/build/db

# Add custom config
ADD rippled.cfg /opt/rippled/build/rippled.cfg

CMD ["/opt/rippled/build/rippled", "--net", "--conf", "/opt/rippled/build/rippled.cfg"]
