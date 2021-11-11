FROM jarischaefer/baseimage-ubuntu:3.1-1

ARG COMPOSER_VERSION
ARG NET_IPV4_VERSION
ARG NET_IPV6_VERSION

ADD pre_install /

RUN chmod +x /build/install && /build/install && rm -r /build
