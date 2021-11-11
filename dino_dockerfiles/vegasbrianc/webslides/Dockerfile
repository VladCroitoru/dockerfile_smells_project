FROM nginx:alpine

MAINTAINER Brian Christner <brian.christner@gmail.com>

WORKDIR /usr/share/nginx/html

RUN set -x \
	&& apk update && apk upgrade \
	&& apk add --no-cache curl tar \
	&& curl -sSL https://github.com/jlantunez/webslides/archive/master.tar.gz | tar -xvz --strip-components=1

EXPOSE 80
