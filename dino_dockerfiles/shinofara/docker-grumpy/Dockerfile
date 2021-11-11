FROM golang:latest

WORKDIR /tmp
RUN apt-get install -y git

WORKDIR /src
RUN git clone https://github.com/google/grumpy \
    && cd /src/grumpy \
    && make

RUN apt-get --purge remove -y git \
    && apt-get clean

ENV GOPATH /src/grumpy/build
ENV PYTHONPATH /src/grumpy/build/lib/python2.7/site-packages

WORKDIR /work
RUN mv /src/grumpy/tools/grumpc /usr/bin/grumpc