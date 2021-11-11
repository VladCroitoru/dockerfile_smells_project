FROM node:7.5.0

ENV CLIENT_DIR /usr/src/client

RUN npm install --global @angular/cli && npm install --global typings

WORKDIR $CLIENT_DIR
COPY package.json $CLIENT_DIR/package.json
COPY typings.json $CLIENT_DIR/typings.json
RUN npm install && typings install
COPY . $CLIENT_DIR

WORKDIR $CLIENT_DIR

EXPOSE 4200 49152

WORKDIR $CLIENT_DIR

CMD ['ng serve', '--ssl true', '--ssl-key /usr/src/app/cert.key', '--ssl-cert /usr/src/app/cert.crt', '--host 0.0.0.0']
