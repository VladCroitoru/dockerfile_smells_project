FROM ubuntu:14.04

RUN apt-get update && apt-get install -y \
 git build-essential bsdmainutils libunbound-dev cmake \
 libevent-dev libgtest-dev curl wget nano sudo \
 cmake gdebi

WORKDIR /tmp
RUN wget http://cz.archive.ubuntu.com/ubuntu/pool/universe/b/boost1.55/libboost1.55-all-dev_1.55.0-1_amd64.deb
RUN wget http://cz.archive.ubuntu.com/ubuntu/pool/universe/b/boost1.55/libboost1.55-dev_1.55.0-1_amd64.deb
RUN gdebi --non-interactive libboost1.55-dev_1.55.0-1_amd64.deb
RUN gdebi --non-interactive libboost1.55-all-dev_1.55.0-1_amd64.deb
RUN git clone https://github.com/ByteCodeTeam/BitAsean.git

WORKDIR /tmp/BitAsean
RUN make -j 8


RUN mkdir /opt/BitAsean
RUN cp /tmp/BitAsean/build/release/src/* /opt/BitAsean -r

ADD entrypoint.sh /

WORKDIR /opt/BitAsean

EXPOSE 40609

ENTRYPOINT ["/entrypoint.sh"]

CMD ["/opt/BitAsean/BitAsean"]
