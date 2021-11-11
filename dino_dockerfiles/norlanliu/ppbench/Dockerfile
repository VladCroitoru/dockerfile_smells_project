FROM alpine:3.2
MAINTAINER nolan liu <nolan.liu@gmail.com>

ENV BUILD_PACKAGES bash curl-dev ruby-dev build-base
ENV RUBY_PACKAGES ruby ruby-io-console ruby-bundler

RUN apk update && \
    apk upgrade && \
	apk add $BUILD_PACKAGES && \
	apk add $RUBY_PACKAGES && \
	rm -rf /var/cache/apk/*

RUN gem install ppbench

CMD ["top"]
