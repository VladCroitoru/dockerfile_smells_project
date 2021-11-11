FROM maxird/node:7-10

ADD . /app

WORKDIR /app

RUN npm install --production

ENV PORT 80

CMD ["node", "index.js"]
