FROM debian:jessie as builder
MAINTAINER david.varga@realcity.io

# Install build environment for tinyproxy build
RUN    apt-get update \
    && apt-get install -y automake gcc make xsltproc bash asciidoc valgrind git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

RUN git clone https://github.com/tinyproxy/tinyproxy.git /build
RUN  ./autogen.sh \
  && ./configure \
  && make \
  && make install

# Create separate final container for runtime dependencies
FROM debian:jessie

# Install dependencies only
RUN    apt-get update \
    && apt-get install -y bash $(apt-cache depends tinyproxy   | grep Depends | sed "s/.*ends:\ //" | tr '\n' ' ') \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd nobody

COPY --from=builder /usr/local/bin/tinyproxy /usr/local/bin/tinyproxy
COPY --from=builder /usr/local/etc/tinyproxy /usr/local/etc/tinyproxy
COPY entry.sh entry.sh

RUN     sed -i -e 's|^PidFile.*|PidFile "/tmp/tinyproxy.pid"|'       /usr/local/etc/tinyproxy/tinyproxy.conf \
        && echo "Allow  0.0.0.0/0"                                >> /usr/local/etc/tinyproxy/tinyproxy.conf

ENTRYPOINT ["/entry.sh"]

EXPOSE 8888
