FROM node:9.2.0-alpine

ENV JOINTSWP_VERSION 5.0

RUN apk add --no-cache git
RUN apk --no-cache add --virtual native-deps \
      g++ gcc libgcc libstdc++ linux-headers \
      make python curl autoconf automake \
      file nasm zlib-dev && \
    npm install --quiet node-gyp -g && \
    npm install --quiet gulp-cli -g && \
    curl -Lo package.json https://raw.githubusercontent.com/JeremyEnglert/JointsWP/${JOINTSWP_VERSION}/package.json && \
    npm install --quiet && \
    apk del native-deps
