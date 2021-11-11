FROM node:0.10-wheezy

ENV PORT 3000

EXPOSE 3000

ADD . /slackfetch

WORKDIR /slackfetch

RUN npm install

WORKDIR /slackfetch

CMD ["node", "index.js"]
