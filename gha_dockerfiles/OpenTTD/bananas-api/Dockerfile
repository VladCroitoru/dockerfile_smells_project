FROM python:3.8-slim

ARG BUILD_DATE=""
ARG BUILD_VERSION="dev"

LABEL maintainer="OpenTTD Dev Team <info@openttd.org>"
LABEL org.opencontainers.image.created=${BUILD_DATE}
LABEL org.opencontainers.image.authors="OpenTTD Dev Team <info@openttd.org>"
LABEL org.opencontainers.image.url="https://github.com/OpenTTD/bananas-api"
LABEL org.opencontainers.image.source="https://github.com/OpenTTD/bananas-api"
LABEL org.opencontainers.image.version=${BUILD_VERSION}
LABEL org.opencontainers.image.licenses="GPLv2"
LABEL org.opencontainers.image.title="OpenTTD's content service API"
LABEL org.opencontainers.image.description="This is the HTTP API for OpenTTD's content service, called BaNaNaS."

# git is needed to clone BaNaNaS
# openssh-client is needed to git clone over ssh
# wget is temporary needed to download tusd.
RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        openssh-client \
        wget \
    && rm -rf /var/lib/apt/lists/*

# We will be connecting to github.com, so populate their key already.
RUN mkdir -p ~/.ssh \
    && ssh-keyscan -t rsa github.com >> ~/.ssh/known_hosts

RUN wget -q https://github.com/tus/tusd/releases/download/v1.1.0/tusd_linux_amd64.tar.gz \
    && mkdir -p /tusd \
    && tar xf tusd_linux_amd64.tar.gz -C /tusd \
    && mv /tusd/tusd_linux_amd64/tusd /usr/bin/tusd \
    && rm -rf tusd_linux_amd64.tar.gz /tusd \
    && apt-get remove -y wget

WORKDIR /code

COPY requirements.txt \
        LICENSE \
        README.md \
        clients-development.yaml \
        clients-production.yaml \
        clients-staging.yaml \
        /code/
COPY licenses /code/licenses
# Needed for Sentry to know what version we are running
RUN echo "${BUILD_VERSION}" > /code/.version

RUN pip --no-cache-dir install -U pip \
    && pip --no-cache-dir install -r requirements.txt

# Validate that what was installed was what was expected
RUN pip freeze 2>/dev/null > requirements.installed \
        && diff -u --strip-trailing-cr requirements.txt requirements.installed 1>&2 \
        || ( echo "!! ERROR !! requirements.txt defined different packages or versions for installation" \
                && exit 1 ) 1>&2

COPY bananas_api /code/bananas_api

ENTRYPOINT ["python", "-m", "bananas_api"]
CMD ["--bind", "0.0.0.0", "--storage", "local", "--index", "local", "--user", "developer", "--client-file", "clients-development.yaml"]
