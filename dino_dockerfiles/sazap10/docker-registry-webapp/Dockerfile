FROM mhart/alpine-node:5.5.0

WORKDIR /src
ADD . .

RUN deps="git" \
 && apk update \
 && apk add $deps \
 && npm install \
 && npm install -g bower \
 && bower install --allow-root \
 && apk del $deps \
 && rm -rf /var/cache/apk/* \
 && npm cache clean \
 && rm -rf ~/.node-gyp /tmp/npm*

EXPOSE 3000

CMD ["node", "server.js"]