## Dockerfile for api-benchmark

FROM mhart/alpine-node:7
MAINTAINER abu shumon <johnshumon@gmail.com>

VOLUME /api-benchmark/reports && /api-benchmark/test-script
WORKDIR /api-benchmark

COPY package.json .

RUN npm install --production

COPY log/ ./log
COPY server.js .

EXPOSE 8096

CMD ["node", "server.js"]