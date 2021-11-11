FROM lroguet/rpi-home-assistant:latest
MAINTAINER orbsmiv@hotmail.com

RUN [ "cross-build-start" ]

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      default-libmysqlclient-dev \
      libtool \
      autoconf \
      automake \
      git \
  && pip3 install mysqlclient \
  && mkdir /tmp/compile-libcoap \
  && git clone --depth 1 --recursive -b dtls https://github.com/home-assistant/libcoap.git /tmp/compile-libcoap \
  && cd /tmp/compile-libcoap \
  && ./autogen.sh \
  && ./configure --disable-documentation --disable-shared --without-debug CFLAGS="-D COAP_DEBUG_FD=stderr" \
  && make \
  && make install \
  && apt-get purge \
      libtool \
      autoconf \
      automake \
      git \
  && apt-get autoremove \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
  && rm -rf /tmp/compile-libcoap

WORKDIR /

RUN [ "cross-build-end" ]
