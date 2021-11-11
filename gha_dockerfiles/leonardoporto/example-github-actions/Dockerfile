FROM node:16-alpine

COPY package.json ./

RUN yarn install --production

COPY . .

ENTRYPOINT ["yarn", "start"]
