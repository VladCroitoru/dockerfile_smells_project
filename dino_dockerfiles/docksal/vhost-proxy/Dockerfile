FROM openresty/openresty:1.19.3.2-1-alpine

# amd64 / arm64
ARG TARGETARCH

RUN set -xe; \
	apk add --update --no-cache \
		bash \
		curl \
		sudo \
		supervisor \
	; \
	rm -rf /var/cache/apk/*

RUN set -xe; \
	addgroup -S nginx; \
	adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx

ARG DOCKER_VERSION=20.10.7
ARG DOCKER_GEN_VERSION=0.7.6
ARG GOMPLATE_VERSION=3.0.0

# Install docker client binary (if not mounting binary from host)
RUN set -xe; \
	# x86_64 / aarch64
	UNAMEARCH=$(uname -m); \
	curl -sSL -O "https://download.docker.com/linux/static/stable/${UNAMEARCH}/docker-${DOCKER_VERSION}.tgz"; \
	tar zxf docker-$DOCKER_VERSION.tgz; \
	mv docker/docker /usr/local/bin ; \
	rm -rf docker*

# Install docker-gen
ARG DOCKER_GEN_TARFILE=docker-gen-alpine-linux-${TARGETARCH}-$DOCKER_GEN_VERSION.tar.gz
RUN set -xe; \
	curl -sSL -O "https://github.com/nginx-proxy/docker-gen/releases/download/${DOCKER_GEN_VERSION}/${DOCKER_GEN_TARFILE}"; \
	tar -C /usr/local/bin -xvzf $DOCKER_GEN_TARFILE; \
	rm $DOCKER_GEN_TARFILE

# Install gomplate
RUN set -xe; \
	curl -sSL https://github.com/hairyhenderson/gomplate/releases/download/v${GOMPLATE_VERSION}/gomplate_linux-${TARGETARCH}-slim -o /usr/local/bin/gomplate; \
	chmod +x /usr/local/bin/gomplate

RUN set -xe; \
	# Symlink openresety config folder to /etc/nginx to preserver full compatibility with original nginx setup
	rm -rf /etc/nginx && ln -s /usr/local/openresty/nginx/conf /etc/nginx ; \
	mkdir -p /etc/nginx/conf.d ; \
	# Also symlink nginx binary to a location in PATH
	ln -s /usr/local/openresty/nginx/sbin/nginx /usr/sbin/nginx

# Certs
RUN set -xe; \
	apk add --update --no-cache \
		openssl \
	; \
	# Create a folder for custom vhost certs (mount custom certs here)
	mkdir -p /etc/certs/custom; \
	# prepare config for certificate
	echo '[req]' >ext.conf; \
	echo 'distinguished_name=req' >>ext.conf; \
	echo '[ext]' >>ext.conf; \
	echo 'subjectAltName=DNS:docksal,DNS:*.docksal' >>ext.conf; \
	echo 'extendedKeyUsage = clientAuth, serverAuth' >>ext.conf; \
	# Generate a self-signed fallback cert
	# Note: the cert validity is limitted to 2 years (see https://github.com/docksal/service-vhost-proxy/issues/56)
	openssl req \
		-x509 \
		-batch \
		-newkey rsa:4096 \
		-sha256 \
		-days 730 \
		-nodes \
		-subj '/CN=Docksal Project' \
		-keyout /etc/certs/server.key \
		-out /etc/certs/server.crt \
		-extensions ext \
		-config ext.conf; \
	rm -rf ext.conf; \
	apk del openssl && rm -rf /var/cache/apk/*;

COPY conf/nginx/ /etc/nginx/
COPY conf/sudoers /etc/sudoers
# Override the main supervisord config file, since some parameters are not overridable via an include
# See https://github.com/Supervisor/supervisor/issues/962
COPY conf/supervisord.conf /etc/supervisord.conf
COPY conf/crontab /var/spool/cron/crontabs/root
COPY bin /usr/local/bin
COPY www /var/www
COPY healthcheck.sh /opt/healthcheck.sh

# Fix permissions
RUN chmod 0440 /etc/sudoers

ENV \
	# Disable INACTIVITY_TIMEOUT by default
	PROJECT_INACTIVITY_TIMEOUT=0 \
	# Disable DANGLING_TIMEOUT by default
	PROJECT_DANGLING_TIMEOUT=0 \
	# Enable PROJECT_AUTOSTART by default
	PROJECT_AUTOSTART=1 \
	# Disable access log by default
	ACCESS_LOG=0 \
	# Disable debug output by default
	DEBUG_LOG=0 \
	# Disable stats log by default
	STATS_LOG=0 \
	# Default domain
	DEFAULT_CERT=docksal

# Starter script
ENTRYPOINT ["docker-entrypoint.sh"]

# By default, launch supervisord to keep the container running.
CMD ["supervisord"]

# Health check script
HEALTHCHECK --interval=5s --timeout=1s --retries=3 CMD ["/opt/healthcheck.sh"]
