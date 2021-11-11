FROM node:7.8.0-alpine

RUN npm config set production true && \
  npm install pgb-weinre@0.9.1 -g --production

CMD ["weinre", "--boundHost", "0.0.0.0", "--httpPort", "80", "--verbose", "--debug"]
