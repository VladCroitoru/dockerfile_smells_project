FROM node:14

RUN mkdir -p /capitalisk-core

COPY . /capitalisk-core/
WORKDIR /capitalisk-core

RUN npm install

EXPOSE 8001
EXPOSE 8021

CMD ["node", "index.js"]
