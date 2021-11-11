FROM node:6.9.5-alpine

EXPOSE 5001

WORKDIR /

COPY ./core /core
COPY ./package.json /

RUN set -x \
    && mkdir -p theme wp-content/themes/default \
    && npm install

ENTRYPOINT ["node", "/core/cmd.js"]
