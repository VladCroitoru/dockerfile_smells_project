FROM alpine 

RUN echo "http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk update

RUN apk add make gcc g++ ucspi-tcp6 daemontools ca-certificates wget && update-ca-certificates

RUN mkdir /src ; cd /src ; \
    wget -O - https://cr.yp.to/djbdns/djbdns-1.05.tar.gz | tar xzf - ; \
    cd djbdns-1.05 ; \
    echo gcc -O2 -include /usr/include/errno.h > conf-cc ; \
    make && make setup check

RUN tinydns-conf nobody nobody /srv/dns 0.0.0.0 

COPY start.sh /start.sh
COPY rebuild.sh /rebuild.sh

RUN chmod +x /start.sh
RUN chmod +x /rebuild.sh

COPY test.dns /srv/dns/root/data

CMD '/start.sh'

