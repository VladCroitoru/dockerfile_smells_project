FROM alpine:edge

RUN echo '@community http://dl-cdn.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories \
    && apk update \
    && apk add py-gevent@community py-msgpack@community tor@community wget python \
    && rm -rf /var/cache/apk/*

RUN mkdir /zeronet \
    && cd /zeronet \
    && wget --no-check-certificate https://github.com/HelloZeroNet/ZeroNet/archive/master.tar.gz \
    && tar zxvpf master.tar.gz \
    && rm -f master.tar.gz

RUN echo -e "ControlPort 9051\nSocksListenAddress 0.0.0.0\nCookieAuthentication 1\nRunAsDaemon 1" > /etc/tor/torrc

WORKDIR /zeronet/ZeroNet-master

CMD /usr/bin/tor \
    && python zeronet.py --ui_ip 0.0.0.0
