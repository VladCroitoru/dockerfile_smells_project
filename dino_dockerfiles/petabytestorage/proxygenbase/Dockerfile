FROM ubuntu:17.10

# build proxygen version 2018-02-26

MAINTAINER rudi@petabytestorage.com
RUN apt update -y
ENV LD_LIBRARY_PATH /usr/local/lib
ENV LDFLAGS -L/usr/local/lib
ENV CPPFLAGS -I/usr/local/include
RUN apt install -y libboost-all-dev wget sudo build-essential libmysqlclient-dev cmake ccache libcurl4-openssl-dev libcurlpp-dev libjansson-dev lcov libodb-dev odb libodb-mysql-dev
ENV PATH="/usr/lib/ccache:${PATH}"
WORKDIR /root
RUN wget https://github.com/facebook/proxygen/archive/v2018.02.26.00.tar.gz
RUN tar xvfz v2018.02.26.00.tar.gz

RUN wget https://github.com/jbeder/yaml-cpp/archive/yaml-cpp-0.6.1.tar.gz

RUN tar xvfz yaml-cpp-0.6.1.tar.gz

RUN cd /root/yaml-cpp-yaml-cpp-0.6.1 && mkdir build && cd build && cmake .. && make && make install

WORKDIR /root/proxygen-2018.02.26.00

RUN cd proxygen && head --lines=-7 deps.sh >d2.sh && cat d2.sh >deps.sh && rm d2.sh && ./deps.sh
RUN apt clean
WORKDIR /root
