FROM node:12-alpine AS ui-build
RUN apk update && apk add python make g++ && rm -rf /var/cache/apk/*

WORKDIR /usr/src/app
COPY eaas_back/ ./eaas_back
COPY eaas_front/ ./eaas_front

COPY eaas_back/package.json ./eaas_back/
COPY eaas_front/package.json ./eaas_front/


WORKDIR eaas_front
RUN npm install -g @angular/cli@8.3.14
RUN npm install

RUN mkdir -p ../InefBack/public
RUN npm build --prod --output-path ../eaas_back/public/
RUN npm prune --production

WORKDIR ../eaas_back

RUN npm install

CMD ["npm", "start"]
