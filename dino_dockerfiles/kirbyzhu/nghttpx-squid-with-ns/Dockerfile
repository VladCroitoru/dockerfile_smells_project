FROM alpine:edge
# squid 3.5.23
# nghttp2 1.22
RUN  apk add --no-cache --update squid nghttp2 git gcc libnet-dev libpcap-dev libc-dev\
 &&  mkdir -m 777 /config 
 
ENV SERVER_CRT=none SERVER_KEY=none

RUN git clone https://github.com/snooda/net-speeder.git net-speeder
WORKDIR net-speeder
RUN sh build.sh -DCOOKED

RUN mv net_speeder /usr/local/bin/
RUN chmod +x /usr/local/bin/net_speeder

ADD entrypoint.sh /entrypoint.sh

ADD squid.conf     /config/squid.conf
ADD nghttpx.conf   /config/nghttpx.conf

RUN  chmod +x /entrypoint.sh \
 &&  chgrp -R 0 /config \
 &&  chmod -R g+rwX /config 
     
ENTRYPOINT  sh /entrypoint.sh

EXPOSE 8443
