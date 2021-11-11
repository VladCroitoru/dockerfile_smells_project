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
RUN wget https://github.com/beast-dev/beast-mcmc/releases/download/v1.8.3/BEASTv1.8.3.tgz
RUN tar -xvzf BEASTv1.8.3.tgz

RUN cp BEASTv1.8.3/bin/* /usr/local/bin
RUN cp BEASTv1.8.3/lib/* /usr/local/lib

COPY runbeast.sh /tmp/runbeast.sh
RUN chmod ugo+x /tmp/runbeast.sh

ENTRYPOINT ["/tmp/runbeast.sh"]
