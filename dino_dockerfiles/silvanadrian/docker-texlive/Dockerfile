FROM ubuntu:trusty
MAINTAINER Silvan Adrian <hallo@silvanadrian.ch>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y tar \
                   git \
                   curl \
                   nano \
                   wget \
                   dialog \
                   net-tools \
                   build-essential
RUN apt-get install -y python python-dev python-distribute python-pip

COPY texlive.profile /tmp/

RUN  wget -c http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \
  && mkdir texlive \
  && tar -zxf install-tl-unx.tar.gz -C ./texlive --strip-components=1 \
  && cd texlive \
  && sudo ./install-tl -profile /tmp/texlive.profile \
  && cd .. \
  && pip install pygments

ENV PATH /usr/local/texlive/2014/bin/x86_64-linux:$PATH
