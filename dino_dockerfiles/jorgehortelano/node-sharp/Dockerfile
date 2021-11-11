FROM node:current-alpine
LABEL Description="Sharp library compilation and instalation for docker Alpine"

ENV SHARP_VERSION 0.18.1

#Compile Vips and Sharp
RUN	apk --no-cache add libpng librsvg libgsf giflib libjpeg-turbo musl \
	&& apk add vips-dev fftw-dev build-base --update-cache  --repository https://alpine.global.ssl.fastly.net/alpine/edge/testing/  --repository https://alpine.global.ssl.fastly.net/alpine/edge/main \
	&& apk --no-cache add --virtual .build-dependencies g++ make python curl tar gtk-doc gobject-introspection expat-dev glib-dev libpng-dev libjpeg-turbo-dev giflib-dev librsvg-dev  \
	&& su node \
	&& npm install sharp@${SHARP_VERSION} --g --production --unsafe-perm \
	&& chown node:node /usr/local/lib/node_modules -R \
	&& apk del .build-dependencies

