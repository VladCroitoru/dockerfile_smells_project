FROM ubuntu:16.04

ENV CLINGO_VER master

USER root

RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get -y install build-essential git cmake bison gcc re2c \
    && apt-get clean

RUN mkdir /opt/clingo
RUN cd /opt/clingo \
    && git init \
    && git remote add origin https://github.com/potassco/clingo.git \
    && git fetch origin ${CLINGO_VER} \
    && git pull origin ${CLINGO_VER} \
    && git submodule update --init --recursive

WORKDIR /opt/clingo
RUN cmake -H/opt/clingo -B/opt/clingo -DCMAKE_BUILD_TYPE=release \
    && cmake --build /opt/clingo

ENV PATH $PATH:/opt/clingo/bin
