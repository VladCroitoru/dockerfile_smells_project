FROM node:14.17
RUN npm -g install npm@7.24

RUN mkdir -p /application && chown node:node /application

WORKDIR /application
USER node:node

COPY package*.json ./
RUN npm ci --no-fund --no-audit

COPY . ./
RUN npm run build

ARG NODE_ENV=production
RUN test '${NODE_ENV}}' = 'production' && npm prune --production

VOLUME [ "/application" ]
EXPOSE 8080

CMD [ "npm", "start" ]
