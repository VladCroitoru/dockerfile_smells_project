ARG VERSION=latest
FROM ubuntu:$VERSION

MAINTAINER Etienne Prud’homme <e.e.f.prudhomme@gmail.com>

ENV DEBIAN_FRONTEND noninteractive

RUN echo 'APT::Get::Assume-Yes "true";' >> /etc/apt/apt.conf \
    && apt-get update && apt-get upgrade

RUN tac /etc/apt/apt.conf \
    | sed '0,/APT::Get::Assume-Yes "true";/{/APT::Get::Assume-Yes "true";/d;}' \
    | tac > /etc/apt/apt.conf
