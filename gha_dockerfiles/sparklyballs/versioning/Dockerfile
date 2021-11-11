ARG ALPINE_VER="3.14"
FROM alpine:${ALPINE_VER}

# install packages
RUN \
	set -ex \
	&& apk add --no-cache \
		bash \
		curl \
		git \
		grep \
		jq \
		shadow

# add versionging user
RUN \
	set -ex \
	&& groupmod -g 1000 users \
	&& useradd -u 1000 -U -s /bin/false versioning \
	&& usermod -G users versioning

# set workdir
WORKDIR /workdir

# set permissions on workdir
RUN \
	set -ex \
	&& chown -R versioning:versioning .
