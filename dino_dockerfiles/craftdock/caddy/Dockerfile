
FROM dsuite/alpine-base:3.14

ARG DOCKER_IMAGE_CREATED
ARG DOCKER_IMAGE_REVISION

LABEL maintainer="Hexosse <hexosse@gmail.com>" \
    org.opencontainers.image.title="docker-suite dsuite/caddy image" \
    org.opencontainers.image.description="Minimal Alpine image with Caddy server" \
    org.opencontainers.image.authors="Hexosse <hexosse@gmail.com>" \
    org.opencontainers.image.vendor="docker-suite" \
    org.opencontainers.image.licenses="MIT" \
    org.opencontainers.image.url="https://github.com/docker-suite/caddy" \
    org.opencontainers.image.source="https://github.com/docker-suite/caddy" \
    org.opencontainers.image.documentation="https://github.com/docker-suite/caddy/blob/master/Readme.md" \
    org.opencontainers.image.created="${DOCKER_IMAGE_CREATED}" \
    org.opencontainers.image.revision="${DOCKER_IMAGE_REVISION}"

ARG PLUGINS

## Define array of plugins to install
ENV PLUGINS=${PLUGINS}
ENV USER="caddy"


## Create users
RUN \
	# Print executed commands
	set -x \
    # Ensure www-data user exists
    # 82 is the standard uid/gid for "www-data" in Alpine
    # (www-data group already exist in alpine)
    && adduser -u 82 -S -D -s /sbin/nologin -G www-data -g www-data www-data 2>/dev/null \
    # Add caddy user
    && addgroup -g 101 -S caddy 2>/dev/null \
    && adduser -u 101 -S -D -s /sbin/nologin -G caddy -g caddy caddy 2>/dev/null \
    # caddy user must be member of www-data
    && adduser caddy www-data 2>/dev/null \
    # Make caddy user like sudo
    && echo "caddy ALL=(ALL) ALL" >> /etc/sudoers \
    && echo "caddy ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

## Install packages
RUN \
	# Print executed commands
	set -x \
    # Update repository indexes
    && apk-update \
    # Install packages needed by Caddy server
    && apk-install sudo libcap mailcap \
	# Clear apk's cache
	&& apk-cleanup

## set up nsswitch.conf for Go's "netgo" implementation
## - https://github.com/docker-library/golang/blob/1eb096131592bcbc90aa3b97471811c798a93573/1.14/alpine3.12/Dockerfile#L9
RUN [ ! -e /etc/nsswitch.conf ] && echo 'hosts: files dns' > /etc/nsswitch.conf

# See https://caddyserver.com/docs/conventions#file-locations for details
ENV XDG_CONFIG_HOME /config
ENV XDG_DATA_HOME /data

## Copy files
COPY rootfs /

## Install latest version of caddy
RUN chmod +x /usr/local/bin/caddy-install.sh \
    && bash /usr/local/bin/caddy-install.sh

## Add volume to allow persistence
VOLUME ["/config", "/data", "/var/www", "/var/log"]

## Expose http, https and caddy port
EXPOSE 80 443 2019

## Entrypoint
ENTRYPOINT ["/entrypoint.sh", "tini", "--"]
CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
