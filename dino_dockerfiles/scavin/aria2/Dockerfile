FROM alpine:edge
MAINTAINER Morgan Auchede <morgan.auchede@gmail.com>

ENV \
    ARIA2_VERSION=1.31.0-r0

RUN set -x \

    # Prepare system

    && resolve() { echo $(apk search $1 | grep "^$1-$2" | sed -e "s/$1-//g") ; } \

    && apk add -U \

    # Install packages

    && apk add --no-cache --update aria2 \

    # Clean

    && rm -rf \
           /var/cache/apk/*

ENTRYPOINT [ "/usr/bin/aria2c" ]
