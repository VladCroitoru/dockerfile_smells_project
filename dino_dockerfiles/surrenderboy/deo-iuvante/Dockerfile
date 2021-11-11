FROM node:9-alpine
RUN mkdir /app
WORKDIR /app
COPY package.json /app/package.json
COPY package-lock.json /app/package-lock.json
RUN apk add --no-cache make gcc g++ python && \
    npm install && \
    apk del make gcc g++ python
COPY . /app
RUN  npm run build

CMD while sleep 3600; do :; done
