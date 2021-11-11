FROM node:8-alpine
RUN apk update && apk upgrade && \
    apk add --no-cache bash git openssh && \
    npm install -g vue-cli
ENTRYPOINT ["vue", "init"]
