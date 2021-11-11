FROM node:alpine

LABEL maintainer="@mstred"

RUN apk update && apk add yarn --purge \
  && yarn global add create-react-app \
  && create-react-app /tmp/app

COPY start.sh /

ENTRYPOINT /start.sh
