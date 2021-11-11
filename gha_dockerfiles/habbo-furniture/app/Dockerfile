FROM node:12-alpine

EXPOSE 3000

WORKDIR /app
COPY package.json .
COPY yarn.lock .
RUN yarn
COPY . .
RUN yarn build
ENTRYPOINT [ "node", "build/index.js" ]

