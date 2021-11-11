FROM phusion/baseimage:focal-1.0.0-amd64

MAINTAINER Anton Zagorskii <amberovsky@gmail.com>

ENV TERM xterm

ADD ./ /build-layerzero
RUN /build-layerzero/layerzero.sh && rm -rf /build-layerzero
