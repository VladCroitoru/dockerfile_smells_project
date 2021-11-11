FROM node:8.10.0-alpine

ENV WORKDIR="/usr/src/app"

WORKDIR ${WORKDIR}

COPY package.json package-lock.json ./

RUN set -x \
    && npm install

COPY . ./

CMD ["npm", "run", "start"]

EXPOSE 9090
