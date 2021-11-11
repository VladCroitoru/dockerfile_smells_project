FROM alpine:edge

RUN apk add --update nodejs nodejs-npm && npm install npm@latest -g 

#ENV VARIABLES
ENV GHOST_SOURCE /usr/src/app
ENV GHOST_CONTENT /var/lib/ghost
ENV GHOST_VERSION 0.11.11

#Change WORKDIR to ghost directory
WORKDIR $GHOST_SOURCE

RUN apk --no-cache add tar tini \
    && apk --no-cache add --virtual devs gcc make python wget unzip ca-certificates \
    && wget -O ghost.zip https://github.com/TryGhost/Ghost/releases/download/${GHOST_VERSION}/Ghost-${GHOST_VERSION}.zip \
	# && wget -O ghost.zip "https://ghost.org/archives/ghost-${GHOST_VERSION}.zip" \
	&& unzip ghost.zip \
    && npm install node-pre-gyp \
	&& npm install --production \
	&& npm install mysql \
	&& rm ghost.zip \
	&& apk del devs \
	&& npm cache clean --force \
	&& rm -rf /tmp/npm*

#Copy over our configuration filename
COPY ./config.js $GHOST_SOURCE

#Copy over, and grant executable permission to the startup script
COPY ./entrypoint.sh /

RUN chmod +x /entrypoint.sh

EXPOSE 2368

#Run Init System
ENTRYPOINT ["/sbin/tini"]

#Run Startup script
CMD [ "/entrypoint.sh" ]
