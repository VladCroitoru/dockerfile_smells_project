#
# API WSGI runner image
#

#
# From this base image / starting-point
#
FROM alpine:latest

#
# Authorship
#
MAINTAINER Santosh Kumar Gupta <santosh0705@gmail.com>


#
# Copy python dependencies file and application
#
COPY requirements.txt /
COPY api /opt/applications/micro-api/api
COPY wsgi-config.yaml /opt/applications/micro-api
COPY config.cfg.container /opt/applications/micro-api/config.cfg

#
# Install packages
#
RUN set -ex \
    && apk add --no-cache \
        python \
        py-setuptools \
        libpq \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        linux-headers \
        python-dev \
        py-pip \
        postgresql-dev \
    \
    && pip install --no-cache-dir -r /requirements.txt \
    && pip install --no-cache-dir uwsgi \
    \
    && rm -f /requirements.txt \
    && apk del .build-deps

#
# Exposed port on container
#
EXPOSE 8000

#
# Setting working directory
#
WORKDIR /opt/applications/micro-api

#
# Container entrypoint
#
ENTRYPOINT ["uwsgi"]

#
# CMD parameters
#
CMD ["--yaml=wsgi-config.yaml"]
