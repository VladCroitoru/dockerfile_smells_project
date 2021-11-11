##
## ---- Base OS layer ----
## docker build -t styled-screenshots --build-arg IMAGE_SOURCE=node --build-arg IMAGE_TAG=lts --build-arg VERCEL_TOKEN=<token> .
##
ARG IMAGE_SOURCE=node
ARG IMAGE_TAG=lts

FROM ${IMAGE_SOURCE}:${IMAGE_TAG} AS base

## setup base stage
RUN echo "**** Base stage ****"

## setup image arguments
ARG PYTHON_VERSION=3.8.2

ARG VERCEL_TOKEN

ARG USER
ARG UID
ARG GID

ARG NAME="styled-screenshots"
ARG VERSION="$(git describe --abbrev=0 --tag)"
ARG PACKAGE="AlexRogalskiy/screenshots"
ARG DESCRIPTION="Automatically generate styled SVG screenshots upon request"

ARG LC_ALL="en_US.UTF-8"
ARG BUILD_DATE="$(date -u +\"%Y-%m-%dT%H:%M:%SZ\")"
ARG VCS_REF="$(git rev-parse --short HEAD)"

ARG APP_DIR="/usr/src/app"
ARG DATA_DIR="/usr/src/data"
ARG TEMP_DIR="/tmp"

ARG INSTALL_PACKAGES="git curl dumb-init gosu dos2unix locales letsencrypt"

## setup image labels
LABEL "name"="$NAME"
LABEL "version"="$VERSION"
LABEL "description"="$DESCRIPTION"

LABEL "com.github.repository"="https://github.com/${PACKAGE}"
LABEL "com.github.homepage"="https://github.com/${PACKAGE}"
LABEL "com.github.documentation"="https://github.com/${PACKAGE}/blob/master/README.md"
LABEL "com.github.maintainer"="Sensiblemetrics, Inc. <hello@sensiblemetrics.io> (https://sensiblemetrics.io)"

LABEL "com.github.version"="$VERSION"
LABEL "com.github.build-date"="$BUILD_DATE"
LABEL "com.github.vcs-ref"="$VCS_REF"

LABEL "com.github.name"="$NAME"
LABEL "com.github.description"="$DESCRIPTION"

## setup environment variables
ENV PYTHON_VERSION $PYTHON_VERSION

ENV APP_DIR=$APP_DIR \
    DATA_DIR=$DATA_DIR \
    TEMP_DIR=$TEMP_DIR

ENV TZ=UTC \
    LANGUAGE=en_US:en \
    LC_ALL=$LC_ALL \
    LC_CTYPE=$LC_ALL \
    LANG=$LC_ALL \
    PYTHONIOENCODING=UTF-8 \
    PYTHONLEGACYWINDOWSSTDIO=UTF-8 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive \
    APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    NPM_CONFIG_LOGLEVEL=error \
    IN_DOCKER=true

ENV VERCEL_TOKEN $VERCEL_TOKEN

ENV USER=${USER:-'devbot'} \
    UID=${UID:-5000} \
    GID=${GID:-10000}

## create user
RUN addgroup --gid "$GID" "$USER" || exit 0
RUN adduser \
    --disabled-password \
    --gecos "" \
    --ingroup "$USER" \
    --uid "$UID" \
    --shell /bin/bash \
    "$USER" \
    || exit 0

## mount volumes
VOLUME ["$APP_DIR", "$DATA_DIR", "$TEMP_DIR"]

## create working directory
WORKDIR $APP_DIR

## install dependencies
RUN echo "**** Installing build packages ****"
## RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update \
    && apt-get install --assume-yes --no-install-recommends $INSTALL_PACKAGES \
    && apt-get autoclean \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/*

## install python
RUN echo "**** Installing Python ****"
RUN cd /tmp && curl -O https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tar.xz && \
    tar -xvf Python-${PYTHON_VERSION}.tar.xz && \
    cd Python-${PYTHON_VERSION} && \
    ./configure --enable-optimizations && \
    make -j 4 && \
    make altinstall && \
    ln -s /usr/local/bin/python3.8 /usr/bin/python3.8

## install node
RUN echo "**** Installing Node ****"
RUN npm install -g npm && \
    npm install -g vercel

## show versions
RUN echo "npm version: $(npm --version)"
RUN echo "node version: $(node --version | awk -F. '{print $1}')"
RUN echo "python version: $(python3 --version)"

## setup entrypoint
## ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 /usr/local/bin/dumb-init
## RUN chmod +x /usr/local/bin/dumb-init
## ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
ENTRYPOINT ["dumb-init", "--"]
## ENTRYPOINT [ "/usr/bin/tini", "--" ]

## remove cache
RUN echo "**** Cleaning cache ****"

RUN apt-get remove -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev libbz2-dev g++
RUN rm -rf /var/cache/apt/* /tmp/* /var/tmp/*

## copy project files
COPY package.json .

COPY scripts ./scripts

##
## ---- Node Dependencies ----
##
FROM base AS node-dependencies

## setup node modules stage
RUN echo "**** Installing node modules stage ****"

## update npm settings
RUN npm set progress=false && npm config set depth 0

## install only <production> node_modules
## RUN npm install --no-audit --only=prod

## copy production node_modules aside
## RUN cp -R node_modules prod_node_modules

## install node_modules, including 'devDependencies'
RUN npm install --no-audit

## run vercel
RUN yes | vercel --confirm --token $VERCEL_TOKEN

## remove cache
RUN echo "**** Cleaning node cache ****"

RUN npm cache clean --force

##
## ---- Testing ----
##
FROM node-dependencies AS test

## setup testing stage
RUN echo "**** Testing stage ****"

## copy source files
COPY . ./

## run format checking & linting
RUN npm run test:license

##
## ---- Release ----
##
FROM base AS release

## setup release stage
RUN echo "**** Release stage ****"

## copy dependencies
#COPY --from=node-dependencies ${APP_DIR}/prod_node_modules ./node_modules
COPY --from=node-dependencies ${APP_DIR}/node_modules ./node_modules

## copy app sources
COPY . ./

## run scripts
#RUN dos2unix ./scripts/env.sh && \
#    . ./scripts/env.sh

## setup user
USER $USER

## expose port
EXPOSE 3000

## define cmd
CMD [ "npm", "run", "develop:docker" ]
