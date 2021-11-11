FROM node:16-alpine

COPY package*.json /
COPY lib/* /lib/
RUN npm ci --ignore-scripts --production

ENTRYPOINT ["node", "/lib/index.js"]
