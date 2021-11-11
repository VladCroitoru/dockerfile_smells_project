FROM java:8-jdk
ENV GOLANG_VERSION 1.7.5
ENV LV 3.5.1
# gcc for cgo
RUN apt-get update && apt-get install -y --no-install-recommends \
		g++ \
		gcc \
		libc6-dev \
		make \
		curl \
		telnet \
		wget \
		awscli \
		rsync \
		fuse \
		ca-certificates \
	&& rm -rf /var/lib/apt/lists/*

ENV GOLANG_DOWNLOAD_URL https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz
ENV GOLANG_DOWNLOAD_SHA256 2e4dd6c44f0693bef4e7b46cc701513d74c3cc44f2419bf519d7868b12931ac3

RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
	&& echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
	&& tar -C /usr/local -xzf golang.tar.gz \
	&& rm golang.tar.gz

RUN mkdir -p /usr/local/liquibase

ENV GOPATH /builds
ENV LIQUIBASE_HOME /usr/local/liquibase
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH:$LIQUIBASE_HOME

RUN wget https://github.com/liquibase/liquibase/releases/download/liquibase-parent-$LV/liquibase-$LV-bin.tar.gz -O /tmp/liquibase.tar.gz
RUN tar -xf /tmp/liquibase.tar.gz -C /usr/local/liquibase
RUN chmod +x /usr/local/liquibase/liquibase

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"

WORKDIR $GOPATH

RUN wget https://raw.githubusercontent.com/docker-library/golang/master/go-wrapper
RUN mv go-wrapper /usr/local/bin/
RUN curl https://glide.sh/get | sh
RUN go get -u github.com/golang/lint/golint
RUN go get -u github.com/axw/gocov/gocov
RUN go get -u gopkg.in/matm/v1/gocov-html
RUN go get -u github.com/wellington/wellington/wt
RUN go get github.com/rlmcpherson/s3gof3r/gof3r
RUN go get -u github.com/kisielk/errcheck