FROM python:3.8-slim

ARG BUILD_DATE=""
ARG BUILD_VERSION="dev"

LABEL maintainer="OpenTTD Dev Team <info@openttd.org>"
LABEL org.opencontainers.image.created=${BUILD_DATE}
LABEL org.opencontainers.image.authors="OpenTTD Dev Team <info@openttd.org>"
LABEL org.opencontainers.image.url="https://github.com/OpenTTD/DorpsGek"
LABEL org.opencontainers.image.source="https://github.com/OpenTTD/DorpsGek"
LABEL org.opencontainers.image.version=${BUILD_VERSION}
LABEL org.opencontainers.image.licenses="GPLv2"
LABEL org.opencontainers.image.title="DorpsGek"
LABEL org.opencontainers.image.description="DorpsGek is an IRC bot for OpenTTD channels."

WORKDIR /code

COPY requirements.txt \
        LICENSE \
        README.md \
        DorpsGek.conf \
        /code/
# Needed for Sentry to know what version we are running
RUN echo "${BUILD_VERSION}" > /code/.version

RUN pip --no-cache-dir install -U pip \
    && pip --no-cache-dir install -r requirements.txt

# Validate that what was installed was what was expected
RUN pip freeze 2>/dev/null > requirements.installed \
        && diff -u --strip-trailing-cr requirements.txt requirements.installed 1>&2 \
        || ( echo "!! ERROR !! requirements.txt defined different packages or versions for installation" \
                && exit 1 ) 1>&2

COPY dorpsgek /code/dorpsgek
COPY plugins /code/plugins
COPY conf /code/conf

ENTRYPOINT ["python", "-m", "dorpsgek"]
CMD []
