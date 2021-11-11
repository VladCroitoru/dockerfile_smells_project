FROM node:8.10.0
MAINTAINER Shrikant Patnaik <shrikant.patnaik@gmail.com>

ENV BUILD_PACKAGES="build-essential python git curl tar bzip2" \
    NODE_ENV=production \
    PORT=3000

WORKDIR /root/app/bundle

ADD build/app.tar.gz /root/app

RUN apt-get update \
    && apt-get install -y ${BUILD_PACKAGES} \
    && (cd programs/server/ && npm install --unsafe-perm)

EXPOSE 3000
CMD METEOR_SETTINGS=$(cat /root/app/settings/settings.json) node main.js
