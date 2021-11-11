FROM samirfor/csvdedupe-docker

RUN set -ex \
        && apk add --no-cache --virtual .build_scrapy_deps \
                openssl-dev \
                libffi-dev \
                libxml2-dev \
                libxslt-dev \
        && apk add --no-cache --virtual .run_scrapy_deps \
                openssl \
                libffi \
                libxml2 \
                libxslt

ENV SCRAPY_VERSION="1.3.3"

RUN set -ex \
        && ${PIP_INSTALL} scrapy==${SCRAPY_VERSION} \
        && apk del .build_scrapy_deps

RUN set -ex \
        && ${PIP_INSTALL} pymongo

RUN set -ex \
        && ${PIP_INSTALL} python-telegram-handler

# NOTE Pillow’s basic features. Zlib and libjpeg are required by default. Other are optional.
RUN set -ex \
        && apk add --no-cache --virtual .build_pillow_deps \
		libjpeg-turbo \
		libjpeg-turbo-dev \
		zlib \
		zlib-dev \
		tiff \
		tiff-dev \
		openjpeg \
		openjpeg-dev \
		libwebp \
		libwebp-dev \
		freetype \
		freetype-dev \
        && ${PIP_INSTALL} pillow

RUN set -ex \
        && ${PIP_INSTALL} googlemaps

RUN set -ex \
        && ${PIP_INSTALL} python-dateutil dateparser

ENTRYPOINT ["/bin/sh"]
