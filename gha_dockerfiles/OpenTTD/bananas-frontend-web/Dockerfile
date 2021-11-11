FROM node:13 as nodejs

WORKDIR /code

COPY package-lock.json \
        package.json \
        /code/

RUN npm install

FROM python:3.8-slim

ARG BUILD_DATE=""
ARG BUILD_VERSION="dev"

LABEL maintainer="OpenTTD Dev Team <info@openttd.org>"
LABEL org.opencontainers.image.created=${BUILD_DATE}
LABEL org.opencontainers.image.authors="OpenTTD Dev Team <info@openttd.org>"
LABEL org.opencontainers.image.url="https://github.com/OpenTTD/bananas-frontend-web"
LABEL org.opencontainers.image.source="https://github.com/OpenTTD/bananas-frontend-web"
LABEL org.opencontainers.image.version=${BUILD_VERSION}
LABEL org.opencontainers.image.licenses="GPLv2"
LABEL org.opencontainers.image.title="Front-end to the BaNaNaS API"
LABEL org.opencontainers.image.description="This is a front-end for browsing and upload content to OpenTTD's content service, called BaNaNaS."

WORKDIR /code

COPY requirements.txt \
        LICENSE \
        README.md \
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

COPY webclient /code/webclient
COPY --from=nodejs /code/node_modules/tus-js-client/dist/tus.min.js /code/webclient/static/tus.min.js
COPY --from=nodejs /code/node_modules/tus-js-client/dist/tus.min.js.map /code/webclient/static/tus.min.js.map

ENTRYPOINT ["python", "-m", "webclient"]
CMD ["--api-url", "https://api.bananas.staging.openttd.org", "--frontend-url", "http://localhost:5000", "run", "-p", "80", "-h", "0.0.0.0"]
