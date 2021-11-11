FROM daspanel/alpine-base
MAINTAINER Abner G Jacobsen - http://daspanel.com <admin@daspanel.com>

# Set default env variables
ENV \
    # Stop container initialization if error occurs in cont-init.d, fix-attrs.d script's
    S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \

    # Timezone
    TZ="UTC" 

RUN set -ex \
    # Install build packages
    && apk add --no-cache libssl1.0 libcurl \
    && apk add --no-cache --update --virtual=.build-deps \
        bash gcc musl-dev git \
        libressl-dev curl curl-dev python-dev libffi-dev \

    # Install python, pip
    && apk add --no-cache --update python \
    && curl "https://bootstrap.pypa.io/get-pip.py" | python \

    # Install pyCurl
    && export PYCURL_SSL_LIBRARY=openssl \
    && pip install --compile pycurl \

    # Install basic python packages used by Daspanel
    && pip install setproctitle gevent gunicorn \

    # Cleanup
    && apk --purge -v del .build-deps \
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/src \
    && rm -rf /tmp/*

# Inject files in container file system
COPY rootfs /

EXPOSE 5000

