FROM ubuntu:16.04

MAINTAINER Erik van den Bergh, Earlham Institute, Norwich 

RUN apt update
RUN apt install -y vim wget openjdk-8-jre openjdk-8-jdk gcc make autoconf automake libtool subversion pkg-config git

WORKDIR /root

RUN git clone --depth=1 https://github.com/beagle-dev/beagle-lib.git

WORKDIR beagle-lib
RUN ./autogen.sh
RUN ./configure --prefix=/usr/local CPPFLAGS="-mno-avx -mno-avx2"
RUN make install

ENV LD_LIBRARY_PATH=/usr/local/lib

WORKDIR /root
RUN wget https://github.com/CompEvol/beast2/releases/download/v2.4.3/BEAST.v2.4.3.Linux.tgz
RUN tar -xvzf BEAST.v2.4.3.Linux.tgz

RUN cp beast/bin/* /usr/local/bin
RUN cp beast/lib/* /usr/local/lib

COPY runbeast.sh /tmp/runbeast.sh
RUN chmod ugo+x /tmp/runbeast.sh

ENTRYPOINT ["/tmp/runbeast.sh"]
