FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install software-properties-common -y --no-install-recommends
RUN add-apt-repository ppa:ubuntu-toolchain-r/test -y
RUN apt-get update
RUN apt-get install gcc-8 g++-8 libboost-all-dev openjdk-11-jdk git python-pip -y --no-install-recommends
RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-8 100
RUN update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-8 100
RUN pip install setuptools
RUN pip install git+https://github.com/icpc-jag/rime
