FROM buildpack-deps:jessie-scm

# gcc for cgo
RUN apt-get update && apt-get install -y --no-install-recommends \
		g++ \
		gcc \
		libc6-dev \
		make \
		pkg-config \
	&& rm -rf /var/lib/apt/lists/*

#binaries for bootstrap
RUN mkdir /bootstrap
RUN curl -fsSL "https://golang.org/dl/go1.7.3.linux-amd64.tar.gz" -o golang.tar.gz \
	&& echo "508028aac0654e993564b6e2014bf2d4a9751e3b286661b0b0040046cf18028e  golang.tar.gz" | sha256sum -c - \
	&& tar -C /bootstrap -xzf golang.tar.gz \
	&& rm golang.tar.gz

ENV GOROOT_BOOTSTRAP /bootstrap/go

#clone and build
WORKDIR /usr/local
RUN git clone https://go.googlesource.com/go
WORKDIR /usr/local/go/src
RUN /usr/local/go/src/make.bash
RUN ls /usr/local/go/bin

RUN rm -rf /bootstrap

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH
