FROM node:14.17.3-slim

ADD . /opt/lm-nominations

WORKDIR /opt/lm-nominations

RUN rm -rf node_modules .git && npm install

USER nobody

CMD ["node", "app.js"]
