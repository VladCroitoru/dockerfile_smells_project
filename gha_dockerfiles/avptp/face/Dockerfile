## Development image
FROM amd64/node:14.18.0-alpine3.14 AS development

ARG USER_ID=1000
ENV USER_NAME=default
ENV PATH="${PATH}:/usr/src/app/node_modules/.bin"

WORKDIR /usr/src/app

RUN if [ $USER_ID -ne 1000 ]; then \
        apk add --no-cache -t volatile \
            shadow \
     && groupmod -g $USER_ID node \
     && usermod -u $USER_ID -g $USER_ID node \
     && apk del --purge volatile; \
    fi


## Builder image
FROM amd64/node:14.18.0-alpine3.14 AS builder

WORKDIR /usr/src/app

ENV NODE_ENV production
ENV SASS_PATH=node_modules:src

COPY . .

RUN npm ci \
 && npm run build


## Runtime image
FROM nginx:1.20.1-alpine AS runtime

WORKDIR /usr/src/app

COPY chart/files/nginx.conf /etc/nginx/nginx.conf
COPY chart/files/default.conf /etc/nginx/conf.d/default.conf

COPY --from=builder /usr/src/app/build .
