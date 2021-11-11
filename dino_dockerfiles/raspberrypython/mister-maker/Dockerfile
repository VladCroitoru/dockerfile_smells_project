FROM ubuntu:latest
MAINTAINER David Noyes <david@raspberrypython.com>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get -yq upgrade
RUN apt-get install -yq wget \
                        curl \
                        vim \
                        git \
                        tmux \
                        build-essential \
                        autoconf \
                        automake \
                        bison \
                        flex \
                        g++ \
                        libboost-all-dev \
                        libtool \
                        make \
                        pkg-config \
                        ragel \
                        checkinstall

VOLUME ["/workbench"]

CMD ["/bin/bash"]
