# see more things here: https://anonoz.github.io/tech/2018/05/01/rails-dockerfile.html

FROM ruby:2.6-alpine3.9 AS ruby

ARG USER
ARG UID
ARG GID

ENV APP_USER=$USER \
    APP_DIR=/var/app \
    LANG=en_US.utf8 \
    LC_ALL=C.UTF-8 \
    PORT=3030 \
    TZ=UTC

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

# Create default user, home directory and set owner
RUN (getent group ${GID} || addgroup -g ${GID} -S ${APP_USER}) \
    && (getent passwd ${UID} || adduser -S ${APP_USER} -u ${UID} -G `getent group ${GID} | cut -d: -f1`) \
    && mkdir -p ${APP_DIR} \
    && chown -R ${UID}:${GID} ${APP_DIR}

RUN set -ex \
    && apk add --update --no-cache --virtual .app-deps \
        ca-certificates \
        curl \
        file \
        graphicsmagick \
        libpq libsodium \
        postgresql-client \
        tzdata \
        yarn

WORKDIR ${APP_DIR}

ENTRYPOINT [ "config/docker/entrypoint.sh" ]

EXPOSE ${PORT}
CMD []

#################
# BUILDER IMAGE #
#################

FROM ruby AS base

RUN set -ex \
    && apk add --update --no-cache --virtual .build-deps \
        build-base \
        git \
        libc6-compat \
        libffi-dev \
        libsodium-dev \
        musl-dev \
        postgresql-dev


#####################
# DEVELOPMENT IMAGE #
#####################

FROM base AS development

ARG UID
ARG GID
ARG USER

RUN gem install bundler -v "~> 2.0.1" \
    && chown -R ${UID}:${GID} /usr/local/bundle/

USER ${UID}

#################
# BUILDER IMAGE #
#################

FROM base AS builder

ARG UID
ARG GID
ARG USER

ENV NODE_ENV=production \
    RACK_ENV=production \
    RAILS_ENV=production

USER ${UID}

COPY --chown=${UID}:${GID} Gemfile* ./

# RUN gem update --no-document --system \ need sudo
RUN gem install bundler -v "~> 2.0.1" \
    && bundle config --global frozen 1 \
    && bundle install -j 4 --retry 3 --without development test \
    # Remove unneeded files (cached *.gem, *.o, *.c)
    && rm -rf /usr/local/bundle/cache/*.gem \
    && rm -rf /usr/local/bundle/bundler/gems/*/.git \
    && find /usr/local/bundle/gems/ -name "*.c" -delete \
    && find /usr/local/bundle/gems/ -name "*.o" -delete


####################
# PRODUCTION IMAGE #
####################

FROM ruby AS production

ARG UID
ARG GID
ARG USER

ENV RACK_ENV=production \
    RAILS_ENV=production

USER ${UID}

COPY --from=builder --chown=${UID}:${GID} /usr/local/bundle /usr/local/bundle

COPY --chown=${UID}:${GID} . .
