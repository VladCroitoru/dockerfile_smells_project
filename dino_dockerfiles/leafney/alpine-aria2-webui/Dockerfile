FROM alpine:latest
MAINTAINER leafney "babycoolzx@126.com"

ENV WEBUI_PORT 6801
ENV RPC_LISTEN_PORT 6800
ENV BT_LISTEN_PORT 51413
ENV DHT_LISTEN_PORT 51415

RUN apk add --no-cache aria2 busybox unzip supervisor busybox-extras \
	&& echo "files = /etc/aria2/start.ini" >> /etc/supervisord.conf \
	&& adduser -D aria2 \
	&& mkdir -p /etc/aria2 \
	&& mkdir -p /aria2down \
	&& mkdir -p /home/aria2/logs \
	&& rm -rf /var/lib/apk/lists/*

# gosu version
ENV GOSU_VERSION 1.11

# gosu install latest
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
# verify the signature
	export GNUPGHOME="$(mktemp -d)"; \
#	gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4; \
#	gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \
#	command -v gpgconf && gpgconf --kill all || :; \
	rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc; \
	\
# clean up fetch dependencies
	apk del --no-network .gosu-deps; \
	\
	chmod +x /usr/local/bin/gosu; \
# verify that the binary works
	gosu --version; \
	gosu nobody true

# webui-aria2
RUN aria2c https://github.com/ziahamza/webui-aria2/archive/master.zip -o /home/aria2/master.zip \
	&& unzip /home/aria2/master.zip -d /home/aria2/ \
	&& rm /home/aria2/master.zip

# aria2.conf and start.ini
COPY ./etc /etc/aria2/

# create aria2.session
RUN touch /etc/aria2/aria2.session

VOLUME /aria2down

# set dir primition (use `aria2:aria2` or can use user uid: id aria2)
RUN chown -R aria2:aria2 /home/aria2 \
	&& chown -R aria2:aria2 /aria2down \
	&& chown -R aria2:aria2 /etc/aria2

EXPOSE $WEBUI_PORT $RPC_LISTEN_PORT $BT_LISTEN_PORT $DHT_LISTEN_PORT

CMD ["supervisord", "-c", "/etc/supervisord.conf"]

