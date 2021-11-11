FROM alpine:latest

LABEL maintainer="Roberto Schiavone <robertoschiavone@users.noreply.github.com>"

COPY entrypoint.sh /entrypoint.sh

RUN apk add --no-cache curl
RUN apk add --no-cache jq

ENTRYPOINT ["/entrypoint.sh"]
