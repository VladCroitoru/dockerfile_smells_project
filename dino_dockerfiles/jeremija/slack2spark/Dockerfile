FROM node:8-alpine

ENV APP_DIR=/app

RUN addgroup -S app && adduser -S -g app app
RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

COPY package.json package-lock.json ./
RUN npm install
COPY . .

USER app
EXPOSE 3000

CMD ["node", "index.js"]
