FROM ubuntu:14.04
MAINTAINER Erik Kaareng-Sunde <esu@enonic.com>

RUN apt-get update && apt-get -y install tcpdump wget curl git build-essential gcc g++ automake autoconf libpcap-dev libboost-dev libssl-dev zlib1g-dev libcairo2-dev 

RUN cd /tmp ; wget http://digitalcorpora.org/downloads/tcpflow/tcpflow-1.4.5.tar.gz
RUN cd /tmp ; tar zxvf tcpflow-1.4.5.tar.gz
RUN cd /tmp/tcpflow-1.4.5 ; ./configure
RUN cd /tmp/tcpflow-1.4.5 ; make
RUN cd /tmp/tcpflow-1.4.5 ; make install

ADD launcher.sh /usr/local/bin/launcher.sh
RUN chmod +x /usr/local/bin/launcher.sh

VOLUME  [ "/data" ]

CMD [ "/usr/sbin/tcpdump", "-C", "1000", "-W", "100", "-v", "-w", "/data/dump" ]