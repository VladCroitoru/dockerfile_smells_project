FROM lsiobase/alpine:3.7 as builder

RUN apk add --no-cache --virtual=build-dependencies \
        autoconf \
        automake \
        boost-dev \
        cmake \
        curl \
        file \
        g++ \
        geoip-dev \
        go \
        git \
        libtool \
        make

COPY Reflection /root/go/src/github.com/h31/Reflection

RUN     cd /root/go/src/github.com/h31/Reflection/reflection; \
        go get .; \
        go build -o main -ldflags '-extldflags "-static"' .; \
        mv main /tmp/; \
        cd /tmp; \
        rm -rf /root/go/src/github.com/h31/Reflection/; \
        apk del --purge \
        build-dependencies

#RUN go get -a -ldflags '-extldflags "-static"' github.com/h31/Reflection/reflection

FROM linuxserver/qbittorrent
COPY services.d /etc/services.d
COPY --from=builder /tmp/main /tmp/main
RUN chmod +x /tmp/main
