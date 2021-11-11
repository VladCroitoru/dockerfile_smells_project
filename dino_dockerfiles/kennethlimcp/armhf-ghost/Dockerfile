FROM kennethlimcp/armv7hf-debian-qemu:latest

RUN [ "cross-build-start" ]

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user

RUN apt-get update && apt-get install -y \
		ca-certificates \
		wget \
		curl \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

# grab gosu for easy step-down from root
ENV GOSU_VERSION 1.7
RUN set -x \
	&& wget -O /usr/local/bin/gosu "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture)" \
	&& wget -O /usr/local/bin/gosu.asc "https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg --print-architecture).asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
	&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
	&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
	&& chmod +x /usr/local/bin/gosu \
	&& gosu nobody true

ENV GHOST_SOURCE /usr/src/ghost
WORKDIR $GHOST_SOURCE

# Install Node
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install -y nodejs
#RUN ln -s /usr/bin/nodejs /usr/bin/node
#RUN apt-get install -y npm

ENV GHOST_VERSION 0.11.11

RUN buildDeps=' \
	node-gyp \
	build-essential \
	python-software-properties \
	g++ \
	gcc \
	make \
	python \
	unzip \
	' \
	&& set -x \
	&& apt-get update && apt-get install -y $buildDeps --no-install-recommends && rm -rf /var/lib/apt/lists/* \
	&& wget -O ghost.zip "https://github.com/TryGhost/Ghost/releases/download/${GHOST_VERSION}/Ghost-${GHOST_VERSION}.zip" \
	&& unzip ghost.zip \
	&& npm install --production \
	&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false -o  APT::AutoRemove::SuggestsImportant=false $buildDeps \
	&& rm ghost.zip \
	&& npm cache clean \
	&& rm -rf /tmp/npm*

ENV GHOST_CONTENT /var/lib/ghost
RUN mkdir -p "$GHOST_CONTENT" && chown -R user:user "$GHOST_CONTENT"
VOLUME $GHOST_CONTENT

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

RUN [ "cross-build-end" ]

EXPOSE 2368
CMD ["npm", "start"]
