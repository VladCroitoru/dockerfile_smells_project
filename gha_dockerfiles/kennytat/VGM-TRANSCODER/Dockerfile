FROM golang:1.16-buster as builder

ENV GOPATH /go
ENV CGO_ENABLED 0
ENV GO111MODULE on

RUN \
    apt-get update && apt install -y git make bash s3fs iputils-ping && \
    git clone --branch v0.8.0 https://github.com/ipfs/go-ipfs

RUN cd go-ipfs && \
    go get github.com/ipfs/go-ds-s3@latest && \
    echo "s3ds github.com/ipfs/go-ds-s3/plugin 0" >> plugin/loader/preload_list && \
    make build

RUN cd go-ipfs && make install

# RUN ipfs init

RUN apt-get install -y zsh

RUN mkdir -p /var/s3

RUN mkdir -p /ipfs-config

WORKDIR /data/ipfs

EXPOSE 4001
EXPOSE 5001
EXPOSE 8080

# ENTRYPOINT ["ipfs"]

# ENTRYPOINT ["/bin/bash"]
COPY /ipfs-config/docker-entrypoint.sh /ipfs-config

# COPY config /root/.ipfs
COPY /ipfs-config/config /ipfs-config
# COPY config /
RUN chmod +x /ipfs-config/docker-entrypoint.sh

ENTRYPOINT ["/ipfs-config/docker-entrypoint.sh"]

CMD ["ipfs", "daemon", "--init", "--init-config", "/ipfs-config/config"]
# CMD ["ipfs", "daemon"]
