FROM node:14-alpine

RUN mkdir /home/node/app/ && chown -R node:node /home/node/app

WORKDIR /home/node/app

COPY --chown=node:node package*.json ./

USER node

RUN npm install --only=production && npm cache clean --force --loglevel=error

COPY --chown=node:node . .

ARG DB_ARG

ENV DB_URL ${DB_ARG}

ARG IP_ARG

ENV IP_ADDRESS ${IP_ARG}

ARG SECRET_PRD

ENV SECRET_PROD ${SECRET_PRD}

ARG env

ENV ENVIRONMENT ${env}

CMD ["npm","run","start"]

EXPOSE 3004