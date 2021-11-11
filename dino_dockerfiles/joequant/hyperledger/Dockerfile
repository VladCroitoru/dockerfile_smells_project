# Dockerfile for Hyperledger base image, with everything to go!
# Data is stored under /var/hyperledger/db and /var/hyperledger/production
# Under $GOPATH/bin, there are two config files: core.yaml and config.yaml.

FROM library/ubuntu:xenial
MAINTAINER Joseph Wang <joequant@gmail.com>

# install go
ENV GOPATH /usr/lib/go-1.6
ENV GOROOT /usr/lib/go-1.6
ENV PATH /opt/gopath/bin:/opt/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

ENV DEBIAN_FRONTEND noninteractive

RUN rm -f /var/lib/apt/lists/*Sources* /var/lib/apt/lists/*universe* \
    && sed -i /universe/d /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y curl \
    &&  curl https://raw.githubusercontent.com/joequant/hyperledger/master/docker-setup.sh | bash
WORKDIR "$GOPATH/bin
