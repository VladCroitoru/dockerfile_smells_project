FROM    node:9.1.0-alpine

ENV     NODE_CONFIG_DIR '/app/config'

RUN     mkdir -p /app/config && mkdir -p /app/ui && mkdir -p /app/src

ADD    ./config /app/config/
ADD    ./ui /app/ui/
ADD    ./src /app/src
ADD    ./package.json /app

RUN     cd /app && npm install --production

EXPOSE 8080
EXPOSE 8443

CMD     ["node", "/app/src/Buckle.js"]
