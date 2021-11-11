FROM node:alpine

RUN apk add --no-cache git vim \
    && mkdir -p /usr/src/app \
    && cd /usr/src/app \
    && git clone https://github.com/stephomi/sculptgl.git \
    && cd sculptgl \
#    && sed -ri -e "s!\\\\\\\\!/!g" /usr/src/app/sculptgl/package.json \
    && npm install yarn \
    && npm install \
    && yarn dev

ADD index.html /usr/src/app/sculptgl

WORKDIR /usr/src/app/sculptgl
EXPOSE 80
CMD node_modules/.bin/webpack-dev-server --disable-host-check --host 0.0.0.0 --port 80
