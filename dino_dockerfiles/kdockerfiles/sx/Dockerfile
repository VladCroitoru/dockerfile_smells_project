FROM debian:9.1 AS base
LABEL maintainer="KenjiTakahashi <kenji.sx>"

RUN apt-get update
RUN apt-get install --no-install-recommends -y \
    nginx \
    libfcgi \
    libyajl2 \
    libcurl3 \
    libssl1.0.2 \
    openssl \
    zlib1g \
    expect
RUN apt-get clean

RUN echo "/usr/local/lib" > '/etc/ld.so.conf.d/local.conf'

FROM base

RUN apt-get update
RUN apt-get install --no-install-recommends -y \
    build-essential \
    file \
    libfcgi-dev \
    libyajl-dev \
    libcurl4-openssl-dev \
    libssl1.0-dev \
    zlib1g-dev

COPY sx-clean /tmp/sx/
WORKDIR /tmp/sx/
RUN ./configure \
    --disable-sxhttpd \
    --prefix '/usr/local' \
    --localstatedir '/var'
RUN make
RUN make install
WORKDIR /

FROM base

COPY --from=1 /usr/local /usr/local
COPY run.sh /usr/local/bin/
COPY create_user /usr/local/bin/

RUN ldconfig

EXPOSE 80 443

VOLUME ["/usr/local/etc/sxserver"]

CMD ["/usr/local/bin/run.sh"]
