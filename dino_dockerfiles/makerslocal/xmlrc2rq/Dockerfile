FROM node:4-slim

COPY . /xmlrc2rq
RUN cd /xmlrc2rq && npm install

WORKDIR /xmlrc2rq
ENTRYPOINT ["node", "index.js"]



