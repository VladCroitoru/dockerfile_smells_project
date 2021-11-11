FROM php:7.1-fpm-alpine

LABEL maintainer "Keng Susumpow"

# Build-time metadata as defined at http://label-schema.org
 ARG BUILD_DATE
 ARG VCS_REF
 ARG VERSION
 LABEL org.label-schema.build-date=$BUILD_DATE \
       org.label-schema.name="Moodle" \
       org.label-schema.description="A Docker container for latest version of Moodle" \
       org.label-schema.url="https://www.opendream.co.th/" \
       org.label-schema.vcs-ref=$VCS_REF \
       org.label-schema.vcs-url="https://github.com/opendream/moodle" \
       org.label-schema.vendor="Opendream Co., Ltd." \
       org.label-schema.version=$VERSION \
       org.label-schema.schema-version="1.0"

ENV MD_ROOT /usr/src/moodle
ENV MD_SHA256 096039fe0d9ac5a0b01044eac0fd56dbc3fc5f35a7ca36b3fe183262bfe9c4f0 
ENV MD_DOWNLOAD_URL https://download.moodle.org/stable33/moodle-latest-33.tgz

RUN apk add --no-cache --virtual .build-deps \
    autoconf build-base gcc libc-dev libtool make \
    libjpeg-turbo-dev libpng-dev libxml2-dev icu-dev \
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install gd zip mysqli opcache xmlrpc soap intl \
    && find /usr/local/lib/php/extensions -name '*.a' -delete \
    && find /usr/local/lib/php/extensions -name '*.so' -exec strip --strip-all '{}' \; \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive \
        /usr/local/lib/php/extensions \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u \
    )" \
    && apk add --virtual .phpext-rundeps $runDeps \
    && apk del .build-deps

RUN { \
        echo 'opcache.memory_consumption=128'; \
        echo 'opcache.interned_strings_buffer=8'; \
        echo 'opcache.max_accelerated_files=4000'; \
        echo 'opcache.revalidate_freq=60'; \
        echo 'opcache.fast_shutdown=1'; \
        echo 'opcache.enable_cli=1'; \
    } > /usr/local/etc/php/conf.d/opcache-recommended.ini

RUN curl -o moodle.tgz -SL $MD_DOWNLOAD_URL \
	  && echo "$MD_SHA256 *moodle.tgz" | sha256sum -c - \
	  && tar -xzf moodle.tgz -C /usr/src/ \
	  && rm moodle.tgz
