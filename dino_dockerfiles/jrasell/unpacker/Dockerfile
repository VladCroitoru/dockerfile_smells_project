#
# docker run --rm -it \
#	-e AWS_DEFAULT_REGION=<aws_region> \
#	-e AWS_ACCESS_KEY_ID=<aws_access_key_id> \
#	-e AWS_SECRET_ACCESS_KEY=<aws_secret_access_key> \
#	unpacker --dryrun --tag_key Name --tag_value packer --region us-east-1
#

FROM alpine:latest
MAINTAINER James Rasell <jamesrasell@gmail.com>

ENV PATH /go/bin:/usr/local/go/bin:$PATH
ENV GOPATH /go

RUN	apk add --no-cache \
	ca-certificates

COPY . /go/src/github.com/jrasell/unpacker

RUN set -x \
	&& apk add --no-cache --virtual .build-deps \
		go \
		git \
		gcc \
		libc-dev \
		libgcc \
	&& cd /go/src/github.com/jrasell/unpacker \
	&& go build -o /usr/bin/unpacker . \
	&& apk del .build-deps \
	&& rm -rf /go \
	&& echo "Build complete."

ENTRYPOINT ["unpacker"]