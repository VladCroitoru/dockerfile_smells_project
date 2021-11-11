FROM ubuntu:xenial

ENV GOLANG_VERSION 1.8
ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_DOWNLOAD_SHA256 53ab94104ee3923e228a2cb2116e5e462ad3ebaeea06ff04463479d7f12d27ca

ENV GOPATH /go
ENV GOBIN /go/bin
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

COPY cloud-watch /go/src/cloud-watch
COPY main.go /go/src/systemd-cloud-watch/main.go
WORKDIR /go/src

RUN apt-get update && \
    apt-get -y install \
        ca-certificates \
        curl \
        gcc \
        git \
        libc6-dev \
        libsystemd-dev \
        pkg-config \
        && \
    curl -fsSL $GOLANG_DOWNLOAD_URL -o golang.tar.gz && \
	echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - && \
	tar -C /usr/local -xzf golang.tar.gz && \
	rm golang.tar.gz && \
    go get ./cloud-watch && \
    go get ./systemd-cloud-watch && \
    apt-get -y purge \
        curl \
        gcc \
        git \
        pkg-config \
        && \
    apt-get -y autoremove && \
    rm -Rf /usr/local/go /go/src/

ENTRYPOINT ["/go/bin/systemd-cloud-watch"]
