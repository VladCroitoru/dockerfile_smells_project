FROM ubuntu:zesty

# gcc for cgo
RUN dpkg --add-architecture i386 && apt-get update && apt-get install -y --no-install-recommends \
		g++ \
		gcc \
		libc6-dev \
		make \
		pkg-config \
		ca-certificates \
		wget \
		git \
		ssh \
		mingw-w64 \
		nsis \
		wine-stable \
		wine32 \
	&& rm -rf /var/lib/apt/lists/*

ENV GOLANG_VERSION 1.9

RUN cd /usr/local && wget https://storage.googleapis.com/golang/go${GOLANG_VERSION}.linux-amd64.tar.gz && \
    tar zxf go${GOLANG_VERSION}.linux-amd64.tar.gz && rm go${GOLANG_VERSION}.linux-amd64.tar.gz && \
    ln -s /usr/local/go/bin/go /usr/bin/

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH
