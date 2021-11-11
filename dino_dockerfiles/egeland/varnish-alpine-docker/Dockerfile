FROM alpine:3.6 as vmod-builder
WORKDIR /build
RUN apk update
RUN apk add --quiet ca-certificates curl wget tar gzip jq
RUN wget -O libvmod-querystring.tgz $(curl -sL https://api.github.com/repos/Dridi/libvmod-querystring/releases/latest | grep 'browser_download_url' | grep '\.tar\.gz' | cut -d '"' -f 4)
RUN tar -zxvf libvmod-querystring.tgz && mv vmod-querystring* libvmod-querystring
RUN apk add --quiet build-base gcc make libtool varnish varnish-dev file python2
WORKDIR /build/libvmod-querystring
RUN ./configure --with-rst2man=: || cat config.log && \
    make && \
    make check && \
    make install

FROM alpine:3.6 as prometheus-exporter-builder

WORKDIR /build
RUN apk update
RUN apk add --quiet ca-certificates curl wget tar gzip jq
RUN curl -sL https://api.github.com/repos/jonnenauha/prometheus_varnish_exporter/releases/latest | jq -r '.assets[] | select(.name | contains ("linux-386.tar.gz")) | .browser_download_url' | xargs wget -O prometheus_varnish_exporter.linux-386.tar.gz
RUN tar -zxvf prometheus_varnish_exporter.linux-386.tar.gz && mv ./prometheus_varnish_exporter-*/prometheus_varnish_exporter /prometheus_varnish_exporter

# Make sure we can run this binary
RUN /prometheus_varnish_exporter -version

FROM hairyhenderson/gomplate as gomplate

FROM alpine:3.6
MAINTAINER  Frode Egeland <egeland@gmail.com>
ENV REFRESHED_AT 2017-11-02
ENV VARNISH_BACKEND_ADDRESS 192.168.1.65
ENV VARNISH_MEMORY 100M
ENV VARNISH_BACKEND_PORT 80
EXPOSE 80
RUN  apk --no-cache add varnish bind-tools tini

# s6 overlay stuff
ENV S6_OVERLAY_VERSION=v1.21.7.0
COPY rootfs /
RUN apk add --no-cache curl \
 && curl -L -s https://github.com/just-containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-amd64.tar.gz \
  | tar xvzf - -C /

COPY --from=vmod-builder /usr/lib/varnish/vmods/libvmod_querystring.so /usr/lib/varnish/vmods/libvmod_querystring.so
COPY --from=gomplate /gomplate /usr/local/bin/gomplate
COPY --from=prometheus-exporter-builder /prometheus_varnish_exporter /usr/local/bin/prometheus_varnish_exporter

ADD *.sh /

ENTRYPOINT [ "/init" ]
