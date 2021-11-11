FROM alpine:3.13

RUN apk update && apk add --update curl libevent-dev build-base gnupg coreutils \
    python3 openssl-dev zstd-dev zlib-dev bash \
    && rm -rf /var/cache/apk/*

WORKDIR /torbuild

COPY get-tor.sh .
RUN chmod +x get-tor.sh && ./get-tor.sh
RUN ./configure --prefix=/usr &&  make

FROM alpine:3.13
RUN apk update && apk add --update libevent openssl zstd \
    && rm -rf /var/cache/apk/*
WORKDIR /tor
COPY --from=0 /torbuild/src/app/tor .

# default port to used for incoming Tor connections
# can be changed by changing 'ORPort' in torrc
EXPOSE 9001

# socks proxy port
EXPOSE 9050

COPY torrc.middle .

VOLUME [ "/tordata" ]
ENTRYPOINT [ "/tor/tor" ]
CMD [ "-f", "/tor/torrc.middle" ]
