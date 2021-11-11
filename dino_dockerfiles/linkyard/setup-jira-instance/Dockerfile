FROM node:7.4.0
MAINTAINER Mario Siegenthaler <mario.siegenthaler@linkyard.ch>

RUN npm install -g -s yarn
RUN npm install -g -s phantomjs

COPY * /usr/src/app/
WORKDIR /usr/src/app
RUN yarn

VOLUME [ "/usr/src/app/logs" ]

CMD [ "node", "index.js" ]
