FROM alpine:3.2
MAINTAINER Chris Heng <bigblah@gmail.com>

RUN apk add -U bash curl tar wget nano rsync gnupg netcat-openbsd build-base ca-certificates \
 && apk add git python nodejs perl openssh-client \
 && rm -rf /var/cache/apk/* \
 && npm install -g node-gyp coffee-script \
 && npm cache clean

ENV PATH node_modules/.bin:$PATH

ENTRYPOINT ["/bin/bash", "-c"]
CMD [""]
