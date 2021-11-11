# Build image

FROM node:12-alpine AS builder

RUN apk --update add ruby imagemagick ca-certificates git

RUN npm install -g sass

ENV APP_USER=3dptools

RUN adduser -D -g "" -G users $APP_USER

COPY src /3dptools
COPY CHANGELOG.md /3dptools/CHANGELOG.md
COPY doc /3dptools/doc
COPY docker/docker_start.sh /docker_start.sh
RUN chown -R $APP_USER:users /docker_start.sh /3dptools && chmod +x /docker_start.sh

WORKDIR /3dptools

RUN apk --update add --virtual 3dpt-dev build-base python krb5-dev sudo && \
    sudo -u $APP_USER yarn install --production && \
    sudo -u $APP_USER yarn cache clean --force

USER $APP_USER

RUN yarn run bower install --production && \
    yarn run bower cache clean
RUN sass public/stylesheets/style.scss public/stylesheets/style.css

# Real image

FROM node:12-alpine

LABEL maintainer="Olivier Robardet <olivier.robardet@gmail.com>"

ENV APP_USER=3dptools

RUN apk add bash
SHELL ["/bin/sh", "-c"]
ENTRYPOINT ["/bin/sh", "-c"]

RUN adduser -D -g "" -G users $APP_USER

COPY --from=builder --chown=$APP_USER:users /3dptools /3dptools
COPY --chown=$APP_USER:users docker/docker_start.sh /docker_start.sh
RUN chmod +x /docker_start.sh

USER $APP_USER
WORKDIR /3dptools

ENV PORT=3000 \
    NODE_ENV=production

ENV database__host=mongo \
    redis__host=redis \
    sentry__dsn="https://88009fc2f595471ea9808336a43e42cd@sentry.io/148531"
# wait for 10 minutes max (120 * 5s) for required services
ENV WAIT_REDIS_MAX_TRIES=120 \
    WAIT_REDIS_TRY_INTERVAL="5s" \
    WAIT_MONGO_MAX_TRIES=120 \
    WAIT_MONGO_TRY_INTERVAL="5s"

EXPOSE $PORT

CMD ["/docker_start.sh"]