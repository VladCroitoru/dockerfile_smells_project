FROM node:16-alpine

WORKDIR /usr/src/smartlist

COPY package.json yarn.lock ./

RUN yarn install --production --frozen-lockfile --no-cache

COPY . .

CMD [ "yarn" , "start" ]

EXPOSE 3000