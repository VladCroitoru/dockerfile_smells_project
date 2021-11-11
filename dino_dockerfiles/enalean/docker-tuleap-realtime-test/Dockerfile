FROM alpine:3.4

MAINTAINER "Juliana Leclaire" <juliana.leclaire@enalean.com>

RUN apk add --no-cache nodejs expect

ENV NODE_ENV dev

VOLUME /nodeapp
WORKDIR /nodeapp

COPY run.sh /run.sh
COPY npm-login.sh /npm-login.sh
ENTRYPOINT ["/run.sh"]
