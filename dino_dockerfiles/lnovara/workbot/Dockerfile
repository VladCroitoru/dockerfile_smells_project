FROM golang:alpine as builder

LABEL maintainer "Luca Novara <luca.n88@gmail.com>"

ENV PATH /go/bin:/usr/local/go/bin:$PATH
ENV GOPATH /go

RUN apk add --no-cache \
	ca-certificates

COPY . /go/src/github.com/lnovara/workbot

RUN set -x \
	&& apk add --no-cache --virtual .build-deps \
		git \
		gcc \
		libc-dev \
		libgcc \
		make \
	&& cd /go/src/github.com/lnovara/workbot \
	&& make static \
	&& mv workbot /usr/bin/workbot \
	&& apk del .build-deps \
	&& rm -rf /go \
	&& echo "Build complete."

FROM alpine

COPY --from=builder /usr/bin/workbot /usr/bin/workbot
COPY --from=builder /etc/ssl/certs/ /etc/ssl/certs
COPY --from=builder /usr/local/go/lib/time/zoneinfo.zip /usr/local/go/lib/time/zoneinfo.zip

ENTRYPOINT [ "workbot" ]
CMD [ "--help" ]
