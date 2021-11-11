FROM php:7.1.11-fpm-alpine3.4

# Supervisord Vars
ENV PYTHON_VERSION=2.7.12-r0
ENV PY_PIP_VERSION=8.1.2-r0
ENV SUPERVISOR_VERSION=3.3.1

# MediaWiki Vars
ENV MEDIAWIKI_MAJOR_VERSION 1.30
ENV MEDIAWIKI_BRANCH REL1_30
ENV MEDIAWIKI_VERSION 1.30.0
ENV MEDIAWIKI_SHA512 ec4aeb08c18af0e52aaf99124d43cd357328221934d593d87f38da804a2f4a5b172a114659f87f6de58c2140ee05ae14ec6a270574f655e7780a950a51178643

# install dependencies via apk
RUN apk update && apk add -u python=$PYTHON_VERSION py-pip=$PY_PIP_VERSION libpng-dev nginx git nodejs

# install supervisord
RUN pip install supervisor==$SUPERVISOR_VERSION

# install php extensions
RUN docker-php-ext-install mysqli json mbstring gd


# Install MEDIAWIKI

# Change working dir
WORKDIR /var/www/html/

RUN mkdir /var/www/data && chown www-data:www-data /var/www/data

RUN  curl -fSL "https://releases.wikimedia.org/mediawiki/${MEDIAWIKI_MAJOR_VERSION}/mediawiki-${MEDIAWIKI_VERSION}.tar.gz" -o mediawiki.tar.gz \
	&& echo "${MEDIAWIKI_SHA512} *mediawiki.tar.gz" | sha512sum -c - \
	&& tar -xz --strip-components=1 -f mediawiki.tar.gz \
	&& rm mediawiki.tar.gz \
  && chown -R www-data:www-data extensions skins cache images

RUN cd extensions \
		&& wget "https://extdist.wmflabs.org/dist/extensions/VisualEditor-${MEDIAWIKI_BRANCH}-61f161a.tar.gz" \
		&& tar -xzf VisualEditor-REL1_30-61f161a.tar.gz

# install parsoid, needed by media wiki to run the visual editor plugin
RUN npm install -g parsoid

# add customer configuration for nginx and supervisord
ADD server-templates/config.yaml /usr/lib/node_modules/parsoid
ADD server-templates/nginx.conf /etc/nginx
ADD server-templates/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisor/conf.d/supervisord.conf"]

EXPOSE  80
