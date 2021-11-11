ARG ALPINE_VER="3.10"
FROM alpine:${ALPINE_VER} as fetch-stage

############## fetch stage ##############

# install fetch packages
RUN \
	apk add --no-cache \
		bash \
		curl

# set shell
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

# fetch version file
RUN \
	set -ex \
	&& curl -o \
	/tmp/version.txt -L \
	"https://raw.githubusercontent.com/sparklyballs/versioning/master/version.txt"

# fetch source code
# hadolint ignore=SC1091
RUN \
	. /tmp/version.txt \
	&& set -ex \
	&& mkdir -p \
		/app/couchpotato \
	&& curl -o \
	/tmp/couchpotato.tar.gz -L \
	"https://github.com/CouchPotato/CouchPotatoServer/archive/${COUCHPOTATO_COMMIT}.tar.gz" \
	&& tar xf \
	/tmp/couchpotato.tar.gz -C \
	/app/couchpotato --strip-components=1

FROM sparklyballs/alpine-test:${ALPINE_VER}

############## runtine stage ##############

# set python to use utf-8 rather than ascii.
ENV PYTHONIOENCODING="UTF-8"

# install runtime packages
RUN \
	apk add --no-cache \
		python \
		py2-lxml \
		py2-openssl

# add artifacts from fetch stage
COPY --from=fetch-stage /app/couchpotato /app/couchpotato

# add local files
COPY root/ /

# ports and volumes
EXPOSE 5050
WORKDIR /app/couchpotato
VOLUME /config /downloads /movies
