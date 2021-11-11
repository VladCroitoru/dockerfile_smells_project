FROM alpine:edge

RUN \
	apk add --no-cache \
		bzip2 \
		cvs \
		docker \
		git \
		gzip \
		mercurial \
		openjdk8-jre-base \
		openssh \
		openssl \
		subversion \
		tar \
		xz \
	&& update-ca-certificates

ADD container-init.sh /usr/local/bin/init

ENTRYPOINT [ "init" ]
EXPOSE 22

