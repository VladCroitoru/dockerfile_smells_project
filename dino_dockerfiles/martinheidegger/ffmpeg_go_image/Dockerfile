FROM jrottenberg/ffmpeg@sha256:bce6df1ec5a67560de76968279e0024f88b259a2b6e5d9b67b8c8462530954a8

# Setup golang
# from: https://github.com/docker-library/golang/blob/d7e2a8d90a9b8f5dfd5bcd428e0c33b68c40cc19/1.5/Dockerfile
# -----------------------------------------------------------------------------------------------------------

ENV \
	GOLANG_DOWNLOAD_URL=https://golang.org/dl/go1.7.4.linux-amd64.tar.gz \
	GOLANG_DOWNLOAD_SHA256=47fda42e46b4c3ec93fa5d4d4cc6a748aa3f9411a2a2b7e08e3a6d80d753ec8b \
	GOPATH=/go

ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

COPY go-wrapper /usr/local/bin/

# gcc for cgo
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		curl \
		wget \
		git \
		time \
		openssl \
		openssh-client \
		ca-certificates \
		libexif-dev \
		imagemagick \
		gifsicle \
		python-setuptools \
		pkg-config \
	&& easy_install qtfaststart \
	&& apt-get install -y --no-install-recommends \
		g++ \
		gcc \
		libc6-dev \
		make \
	&& rm -rf /var/lib/apt/lists/* \
	&& curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
	&& echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
	&& tar -C /usr/local -xzf golang.tar.gz \
	&& rm golang.tar.gz \
	&& mkdir -p "$GOPATH/src" "$GOPATH/bin" \
	&& chmod -R 777 "$GOPATH" \
	&& go get -u github.com/golang/lint/golint \
	&& go get -u github.com/FiloSottile/gvt

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Switch to the src workdir for gvt restore
WORKDIR $GOPATH/src

ENTRYPOINT ["/bin/sh"]

# Copy vendor first to install and cache the dependencies
ONBUILD COPY ./src/vendor $GOPATH/src/vendor

# Get all the dependencies
ONBUILD RUN cd $GOPATH/src/; /bin/bash -c "time gvt restore"

# We assume that the source code is properly in source
ONBUILD COPY src $GOPATH/src

# Add all bin files to the go bin folder
ONBUILD COPY bin $GOPATH/bin

# Add Makefile for eventual builds - culture effort
ONBUILD ADD Makefile $GOPATH

# Switch to /go folder again because the Makefile is in there and it is in
# relation to the source folder as you would have it in a users image
ONBUILD WORKDIR $GOPATH
