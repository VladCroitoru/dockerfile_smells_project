FROM debian:stretch
LABEL maintainer "ant <git@manchestermonkey.co.uk>"

RUN apt-get -qq -y update && \
     apt-get -qq -y install tcpdump && \
     mkdir /pcap && \
     apt-get -qq -y autoremove && \
     apt-get -qq -y clean && \
     rm -Rf /var/lib/apt/lists

WORKDIR /pcap
CMD tcpdump -G 900 -w '%Y-%m-%d_%H:%M:%S.pcap' -W 96
