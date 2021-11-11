FROM ubuntu:rolling

MAINTAINER Jasper Behrensdorf <behrensdorf@irz.uni-hannover.de>

ENV DEBIAN_FRONTEND noninteractive

# Install TeX Live
RUN apt-get update -q && apt-get install -qy \
    texlive-full \
    python-pygments gnuplot \
    make git \
    && rm -rf /var/lib/apt/lists/*
