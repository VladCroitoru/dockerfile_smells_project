FROM mhart/alpine-node:4.8.0

RUN addgroup -g 10001 app && adduser -D -G app -h /app -u 10001 app
USER app
WORKDIR /app

COPY package.json package.json
RUN npm install

EXPOSE 8077
CMD node ./node_modules/.bin/http-server node_modules/http-server -p 8077

