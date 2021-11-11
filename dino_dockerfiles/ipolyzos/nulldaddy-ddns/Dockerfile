FROM golang:1.7.3-alpine
MAINTAINER Ioannis Polyzos <i.polyzos@null-box.org>

ENV GLIDE_VERSION v0.12.3
ENV GLIDE_DOWNLOAD_URL https://github.com/Masterminds/glide/releases/download/$GLIDE_VERSION/glide-$GLIDE_VERSION-linux-amd64.zip

RUN apk update \
    && apk add --update bash \
 	&& apk add curl unzip git -q \
 	&& rm -rf /var/cache/apk/*

RUN curl -fsSL "$GLIDE_DOWNLOAD_URL" -o glide.zip \
	&& unzip glide.zip  linux-amd64/glide \
	&& mv linux-amd64/glide /usr/local/bin \
	&& rm -rf linux-amd64 \
	&& rm glide.zip

ENV GLIDE_HOME /go/src/app

COPY . /go/src/app

ADD run.sh /
RUN chmod +x /run.sh

WORKDIR /go/src/app
ENTRYPOINT ["/run.sh","-daemon"]