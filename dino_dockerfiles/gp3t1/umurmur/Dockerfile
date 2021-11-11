FROM gp3t1/alpine:0.7.3

# UMURMUR BUILD SETTINGS
ARG BUILD_UMURMUR_MONITOR="On"
ARG BUILD_NUMURMON="On"
ARG SSL="openssl"
ARG VERSION="0.2.17"

LABEL maintainer="Jeremy PETIT <jeremy.petit@gmail.com>" \
			description="alpine-based umurmurd image - audio chat server"

## CUSTOM UMURMUR UID/GID
ENV APP_USER="umurmur" 		APP_UID=500
ENV	APP_GROUP="$APP_USER"	APP_GUID=501

## MURMUR BASE CONFIG
ENV LISTEN4="" \
		LISTEN6=""
ENV u_password="" \
		u_adminpassword=""
ENV SHOW_IPS=true \
		ENABLE_BAN=true \
		SYNC_BAN=true \
		ALLOW_TEXT=true \
		LOGGING=false
ENV MAX_USERS=10 \
		BAN_SECONDS=0 \
		MAX_BANDWIDTH=48000 \
		OPUS_THRESHOLD=100
ENV MOTD="Welcome to umurmur server$(hostname -f)!"

## EXPOSE UMURMUR DEFAULT PORT
EXPOSE 64738 64738/udp

## VOLUMES
VOLUME ["/var/log/umurmur", "/var/lib/umurmur"]

## INSTALL USR/GRP TOOLS, BUILD TOOLS, PIP & J2
#  CREATE USER/GROUP
#  INSTALL MURMUR
RUN  apk --no-cache add \
			libconfig \
			openssl \
			protobuf-c \
			py2-pip \
	&&  setAppUser \
	&& apk --no-cache add -t build-dependencies \
			cmake \
			gcc \
			git \
			libc-dev \
			libconfig-dev \
			make \
			ncurses-dev \
			openssl-dev \
			protobuf-c-dev \
	&& pip install --upgrade pip \
	&& pip install --no-cache j2cli[yaml] \
	&& git clone --recursive -b "${VERSION}" "https://github.com/umurmur/umurmur.git" "/tmp/umurmur-src" \
	&& mkdir -p /tmp/umurmur \
	&& cd /tmp/umurmur \
	&& cmake -DSSL="$SSL" -DBUILD_UMURMUR_MONITOR="$BUILD_UMURMUR_MONITOR" -DBUILD_NUMURMON="$BUILD_NUMURMON" "/tmp/umurmur-src" \
	&& make \
	&& make install \
	&& rm -rf /tmp/umurmur* \
	&& mv /usr/local/etc/umurmur.conf /etc/umurmurd.conf.default \
	&& apk --no-cache del build-dependencies

# COPY SCRIPTS & TEMPLATES
COPY bin/* /usr/bin/
COPY templates/* /templates/

# EXTRA INIT SCRIPTS & BAN FILE
RUN mkdir /docker-entrypoint-init.d

CMD ["/usr/local/bin/umurmurd","-d","-c","/etc/umurmurd.conf"]
ENTRYPOINT ["/usr/bin/entrypoint"]

# HEALTHCHECK --interval=1m \
# 	--timeout=3s \
# 	--start-period=30s \
#   --retries=2 \
#   CMD curl -f http://localhost/ || exit 1




