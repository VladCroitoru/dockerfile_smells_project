# https://github.com/mhart/alpine-node/
FROM mhart/alpine-node:8.9.3

COPY . /src

WORKDIR /src

RUN npm install

CMD ["node", "/src/server.js"]
