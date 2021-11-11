FROM golang:latest
MAINTAINER Tomasen "https://github.com/tomasen"

RUN apt-get update && apt-get install -y rsync iperf3 \
  apt-get clean autoclean && \
  apt-get autoremove -y && \
  rm -rf /var/lib/apt/lists/*

# Copy the local package files to the container's workspace.
ADD . /go/src/github.com/tomasen/trafcacc

# change workdir, build and install
WORKDIR /go/src/github.com/tomasen/trafcacc
RUN go get .
RUN go install -race

RUN rm -rf /go/src/*
WORKDIR /go/bin

# you need to run the trafcacc command manually
# ENTRYPOINT /go/bin/trafcacc

# EXPOSE 4043
