FROM node:9-alpine as node

RUN apk --update --no-progress add unrar bash git

VOLUME ["/comics"]
VOLUME ["/data"]

EXPOSE 3001

WORKDIR /app

RUN npm install -g @angular/cli

COPY package.json package.json
COPY package-lock.json package-lock.json

RUN npm install

COPY . .

RUN yarn build

CMD [ "node", "dist/server.js" ]