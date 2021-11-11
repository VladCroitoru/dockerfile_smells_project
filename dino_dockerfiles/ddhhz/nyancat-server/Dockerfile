FROM alpine AS builder

RUN \
    apk upgrade --update && \
    apk add g++ make git autoconf automake

WORKDIR /tmp

RUN \
    git clone https://github.com/boppy/onenetd.git && \
    cd /tmp/onenetd && autoreconf -vfi && ./configure && make && \
    cp ./onenetd /usr/local/bin

WORKDIR /tmp/nyancat

COPY . .

RUN \
    make && \
    cp ./src/nyancat /usr/local/bin/


FROM alpine

LABEL \
    maintainer="Wei He <docker@weispot.com>" \
    verion="1.0" \
    description="Nyancat Telnet Server"

COPY --from=builder /usr/local/bin/onenetd /usr/local/bin/nyancat /usr/local/bin/

EXPOSE 23

ENTRYPOINT ["onenetd", "-v1", "0", "23", "nyancat", "-I", "--telnet"]
