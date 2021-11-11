FROM alpine:latest

ENV UID 1000
ENV USERNAME samba
ENV GID 1000
ENV GROUP samba
ENV PASSWORD password
ENV S6_VERSION 1.21.2.1
ENV S6_ARCH	s6-overlay-amd64
ENV COMMON_SCRIPTS_LOCATION	/opt

#	no longer uses add command to follow dockerfile's good practices
#	Download s6-overlay's files
#	ADD https://keybase.io/justcontainers/key.asc /tmp/key.asc
#	ADD https://github.com/just-containers/s6-overlay/releases/download/v$S6_VERSION/$S6_ARCH.tar.gz /tmp/s6.tar.gz
#	ADD https://github.com/just-containers/s6-overlay/releases/download/v$S6_VERSION/$S6_ARCH.tar.gz.sig /tmp/s6.sig

#	Install packages
RUN set -xe \
	&& apk add --update --no-cache \
	samba-common-tools \
	samba-server \
	gnupg \
	curl

#	Create directory and download common file
RUN set -xe \
	&& mkdir -p $COMMON_SCRIPTS_LOCATION \
	&& curl -o $COMMON_SCRIPTS_LOCATION/createuser.sh -L https://raw.githubusercontent.com/axelhenry/shell-commons/master/docker/alpine_createUser.sh

#	Download s6-overlay files
#	&& curl -o /tmp/key.asc https://keybase.io/justcontainers/key.asc \
RUN set -xe \
	&& curl https://keybase.io/justcontainers/key.asc | gpg --import \
	&& curl -o /tmp/$S6_ARCH.tar.gz -L https://github.com/just-containers/s6-overlay/releases/download/v$S6_VERSION/$S6_ARCH.tar.gz \
	&& curl -o /tmp/$S6_ARCH.tar.gz.sig -L https://github.com/just-containers/s6-overlay/releases/download/v$S6_VERSION/$S6_ARCH.tar.gz.sig

#	Verify s6-overlay' signature and untar
#	&& gpg --import /tmp/key.asc \
RUN set -xe \
	&& gpg --verify /tmp/$S6_ARCH.tar.gz.sig /tmp/$S6_ARCH.tar.gz \
	&& tar xzf /tmp/$S6_ARCH.tar.gz -C / \
	&& rm -rf /tmp /root/.gnupg

#	Remove no longer needed packages
RUN set -xe \
	&& apk del gnupg curl

COPY create-samba-users.s6 /etc/cont-init.d/00-create-samba-users.sh
COPY create-tmp-folder.s6 /etc/cont-init.d/01-create-tmp-folder.sh
COPY run-samba-server.s6 /etc/services.d/samba/run

EXPOSE 137/udp 138/udp 139/tcp 445/tcp

VOLUME ["/config", "/shared"]

CMD ["/init"]
