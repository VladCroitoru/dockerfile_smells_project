FROM alpine
LABEL maintainer="Will Squire <will@willsquire.com>"
WORKDIR /app
RUN apk add yarn --no-cache &&\
    yarn global add polymer-cli &&\
    yarn cache clean
