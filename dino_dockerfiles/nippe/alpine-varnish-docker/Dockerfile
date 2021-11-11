FROM alpine:latest

ENV VERSION="4.1.3"

RUN apk add --update curl make gcc g++ python linux-headers py-docutils ncurses ncurses-dev pcre pcre-dev libedit libedit-dev && \
  curl -sSL https://repo.varnish-cache.org/source/varnish-${VERSION}.tar.gz | tar -xz && \
  cd /varnish-${VERSION} && \
  ./configure && \
  make CPPFLAGS=-D__NEED_mode_t -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \
  make install && \
  cd / && \
  apk del curl make gcc g++ python linux-headers py-docutils ncurses-dev pcre-dev libedit-dev && \
  rm -rf /etc/ssl /varnish-${VERSION} /usr/include /usr/share/man /tmp/* /var/cache/apk/*

RUN apk update
RUN apk add gcc
RUN apk add libc-dev
RUN apk add curl

# Make our custom VCLs available on the container
ADD default.vcl /etc/varnish/default.vcl

# ENV VARNISH_BACKEND_PORT 3000
# ENV VARNISH_BACKEND_IP 192.168.99.100
# ENV VARNISH_PORT 80
# Expose port 80
# EXPOSE 80

# Expose volumes to be able to use data containers
VOLUME ["/var/lib/varnish", "/etc/varnish"]

ADD start.sh /start.sh
CMD ["/start.sh"]
