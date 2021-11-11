# See http://training.play-with-docker.com/node-zeit-pkg/

FROM node:latest AS build

RUN npm install -g pkg pkg-fetch
ENV NODE node8
ENV PLATFORM alpine
ENV ARCH x64
RUN /usr/local/bin/pkg-fetch ${NODE} ${PLATFORM} ${ARCH}

RUN mkdir -p /usr/src/app/release
WORKDIR /usr/src/app

COPY package.json .
COPY package-lock.json .
RUN npm install
COPY . /usr/src/app
RUN npm run build:dist && pkg -t ${NODE}-${PLATFORM}-${ARCH} --output tournament release/index.js

FROM alpine:latest

ENV NODE_ENV=production

RUN addgroup -S siggame && adduser -S -G siggame siggame \
    && apk update && apk add --no-cache libstdc++ libgcc \
    && mkdir -p /app/output && chown -R siggame:siggame /app

COPY --from=build --chown=siggame:siggame /usr/src/app/tournament /app/tournament

USER siggame
WORKDIR /app

CMD ["/app/tournament"]
