FROM golang:1.5
MAINTAINER Brian DeHamer <brian@dehamer.com>

RUN apt-get update && \
  apt-get install -y upx-ucl && \
  apt-get clean &&  \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install Docker binary
RUN wget -nv https://get.docker.com/builds/Linux/x86_64/docker-1.3.3 -O /usr/bin/docker && \
  chmod +x /usr/bin/docker
RUN go get github.com/pwaller/goupx

VOLUME /src
WORKDIR /src

COPY build.sh /

ENTRYPOINT ["/build.sh"]
