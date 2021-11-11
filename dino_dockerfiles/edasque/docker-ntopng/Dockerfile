FROM ubuntu:18.04

LABEL maintainer="Erik Dasque"

RUN apt-get update
RUN apt-get -y -q install curl

RUN apt-get update

RUN apt-get -y -q install net-tools ethtool inetutils-ping libnuma1 dkms \
redis-server librrd8 logrotate libpcap0.8 libhiredis0.13 \
libssl1.0.0 libmysqlclient20 librdkafka1 libcap2 bridge-utils libnetfilter-conntrack3 \
n2n libradcli4 udev libzmq5 libnetfilter-queue1 \
libmaxminddb0 libmaxminddb-dev mmdb-bin

RUN curl -s --remote-name http://packages.ntop.org/apt/18.04/x64/ndpi_2.7.0-1458_amd64.deb
RUN dpkg -i ndpi_2.7.0-1458_amd64.deb

RUN curl -s --remote-name http://packages.ntop.org/apt/18.04/x64/pfring_7.5.0-2355_amd64.deb
RUN dpkg -i pfring_7.5.0-2355_amd64.deb

RUN curl -s --remote-name http://packages.ntop.org/apt/18.04/all/pfring-dkms_7.5.0_all.deb
RUN dpkg -i pfring-dkms_7.5.0_all.deb

RUN curl -s --remote-name http://packages.ntop.org/apt/18.04/x64/ntopng_3.9.181231-5856_amd64.deb
RUN dpkg -i ntopng_3.9.181231-5856_amd64.deb

RUN rm -rf *.deb

RUN apt-get -y -q install ntopng  

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 3000

RUN echo '#!/bin/bash\n/etc/init.d/redis-server start\nntopng "$@"' > /tmp/run.sh
RUN chmod +x /tmp/run.sh

ENTRYPOINT ["/tmp/run.sh"]
