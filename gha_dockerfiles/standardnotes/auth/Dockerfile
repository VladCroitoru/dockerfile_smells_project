FROM node:16.11.1-alpine3.14

ARG UID=1001
ARG GID=1001

RUN addgroup -S auth -g $GID && adduser -D -S auth -G auth -u $UID

RUN apk add --update --no-cache \
    curl \
    alpine-sdk \
    python3

WORKDIR /var/www

RUN chown -R $UID:$GID .

USER auth

COPY --chown=$UID:$GID package.json yarn.lock /var/www/

RUN yarn install --pure-lockfile

COPY --chown=$UID:$GID . /var/www

RUN yarn build

ENTRYPOINT [ "docker/entrypoint.sh" ]

CMD [ "start-web" ]
