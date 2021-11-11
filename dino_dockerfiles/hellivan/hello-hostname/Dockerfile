FROM node:7.9.0-alpine

ENV base /srv/app
WORKDIR ${base}

ENV PORT 8080
EXPOSE 8080

ADD . ./

RUN yarn

CMD ["node", "index.js"]