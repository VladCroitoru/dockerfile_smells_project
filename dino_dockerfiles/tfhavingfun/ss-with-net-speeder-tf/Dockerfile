# shadowsocks-net-speeder

FROM ubuntu:14.04
MAINTAINER tfhavingfun <tftylerfoo@gmail.com>
RUN apt-get update && apt-get install -y \
    python-software-properties \
    software-properties-common \
 && add-apt-repository ppa:chris-lea/libsodium \
 && apt-get update \
 && apt-get install -y python-pip libsodium-dev libnet1 libnet1-dev libpcap0.8 libpcap0.8-dev git

RUN pip install git+https://github.com/shadowsocks/shadowsocks.git@2.9.0#egg=shadowsocks

RUN git clone https://github.com/snooda/net-speeder.git net-speeder
WORKDIR net-speeder
RUN sh build.sh

RUN mv net_speeder /usr/local/bin/
COPY entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/net_speeder

# Configure container to run as an executable
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
