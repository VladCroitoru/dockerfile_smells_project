FROM alpine:latest

RUN addgroup alpine-user && adduser -SDHG alpine-user alpine-user

RUN apk update && \
    apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip connexion && \
    apk add --update curl && \
    apk add --update nodejs nodejs-npm && npm install npm@latest -g && \
    apk del py-pip

WORKDIR /data
RUN chown alpine-user /data
RUN mkdir -p /home/alpine-user && \
  chown alpine-user /home/alpine-user

ENTRYPOINT /bin/sh
