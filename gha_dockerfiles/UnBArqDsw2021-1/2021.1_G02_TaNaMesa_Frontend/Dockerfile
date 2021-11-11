FROM node:alpine

WORKDIR /app

COPY frontend/package.json /app

RUN apk update \
    && apk add --no-cache git \
    && yarn install

COPY frontend/ /app

EXPOSE 3000

CMD [ "/bin/sh", "-c", "yarn build && yarn serve" ]
