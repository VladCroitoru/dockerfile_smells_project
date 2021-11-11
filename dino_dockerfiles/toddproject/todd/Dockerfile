FROM golang:1.9 AS build
MAINTAINER Matt Oswalt <matt@keepingitclassless.net> (@mierdin)

LABEL version="0.1"

env PATH /go/bin:$PATH

RUN mkdir /etc/todd

RUN mkdir -p /opt/todd/agent/assets/factcollectors
RUN mkdir -p /opt/todd/server/assets/factcollectors
RUN mkdir -p /opt/todd/agent/assets/testlets
RUN mkdir -p /opt/todd/server/assets/testlets

# Install ToDD
COPY . /go/src/github.com/toddproject/todd

RUN cd /go/src/github.com/toddproject/todd && GO15VENDOREXPERIMENT=1 make && make install

RUN cp /go/src/github.com/toddproject/todd/etc/* /etc/todd

# Create runtime container
FROM debian:jessie

RUN mkdir /etc/todd && \
    mkdir -p /opt/todd/agent/assets/factcollectors && \
    mkdir -p /opt/todd/agent/assets/testlets && \
    mkdir -p /opt/todd/server/assets/factcollectors && \
    mkdir -p /opt/todd/server/assets/testlets

RUN apt-get update && \
    apt-get -y install --no-install-recommends curl iperf && \
    apt-get -y clean

COPY --from=build /go/bin/todd* /usr/local/bin/

COPY --from=build /etc/todd/* /etc/todd/

CMD ["/usr/local/bin/todd"]
