# bland328/node-red-plus-avahi Dockerfile
#
# Node-RED Dockerfile with integrated Avahi to support node-red-contrib-homekit-bridged
#
# Build for use with Unraid, but know of no specific provisions that would preclude other uses
#
# Based heavily upon https://github.com/mschm/node-red-contrib-homekit/issues/8#issuecomment-362029068
#
# Build reminders to myself, as I don't deal with this very often:
#   1) AUTOBUILD IS ON AT https://cloud.docker.com/swarm/bland328/repository/docker/bland328/node-red-plus-homekit/general
#      SO ANY PUSHED CHANGE HERE RESULTS IN A BUILD BASED ON THE LATEST OFFICIAL NODE-RED DOCKER CONTAINER.
#   2) I also have REPOSITORY LINKS turned on at Docker Hub, so any change to the Base Image (in this case, the
#      official Node-RED Docker Container) would also theoretically result in an auto-build; it is currently unclear
#      whether this nifty Docker Hub feature is broken.
#
# The resulting build is at https://store.docker.com/community/images/bland328/node-red-plus-homekit

# TODO:
#   Consider replacing gosu with su-exec per https://github.com/tianon/gosu/blob/master/INSTALL.md: "Note: when using Alpine, it's probably also worth checking out su-exec (apk add --no-cache su-exec) instead, which since version 0.2 is fully gosu-compatible in a fraction of the file size."

# Overview:
#   Based on offical Node-RED docker
#     + Add gosu (per https://github.com/tianon/gosu/blob/master/INSTALL.md)
#     + Add avahi-daemon
#     + Configure avahi-daemon execution
#     + Add entrypoint.sh

# Declare a Docker image on which to build (2020-01-07: Moved to newer official Node-RED base image)
FROM nodered/node-red:latest

# Become root
USER root

# Download and install gosu (per https://github.com/tianon/gosu/blob/master/INSTALL.md)
ENV GOSU_VERSION 1.11
RUN set -eux; \
	\
	apk add --no-cache --virtual .gosu-deps \
		ca-certificates \
		dpkg \
		gnupg \
	; \
	\
	dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \
	wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"; \
	wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"; \
	\
    # Verify signature
	export GNUPGHOME="$(mktemp -d)"; \
	gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4; \
	gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \
	command -v gpgconf && gpgconf --kill all || :; \
	rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc; \
	\
    # Clean up fetch dependencies
	apk del --no-network .gosu-deps; \
	\
	chmod +x /usr/local/bin/gosu; \
    # Verify binary works
	gosu --version; \
	gosu nobody true
    
# Set gosu ownership and permissions
RUN chown root:node-red /usr/local/bin/gosu && chmod +s /usr/local/bin/gosu

# Install OpenRC init system, avahi-daemon and more
RUN apk add --no-cache \
	openrc \
	dbus \
	make \
	g++ \
	avahi \
	avahi-dev \
	; \
	rm -rf /var/cache/apk/*

# Configure avahi-daemon
RUN sed -i "s/#enable-dbus=yes/enable-dbus=yes/g" /etc/avahi/avahi-daemon.conf && \
	mkdir -p /var/run/dbus && mkdir -p /var/run/avahi-daemon && \
	chown messagebus:messagebus /var/run/dbus && chown avahi:avahi /var/run/avahi-daemon && dbus-uuidgen --ensure

# Become user node-red
USER node-red

# Incorporate entrypoint.sh file, set its permissions, and declare it the entrypoint for the container
COPY entrypoint.sh /usr/src/node-red
RUN gosu root chmod 755 /usr/src/node-red/entrypoint.sh
ENTRYPOINT /usr/src/node-red/entrypoint.sh
