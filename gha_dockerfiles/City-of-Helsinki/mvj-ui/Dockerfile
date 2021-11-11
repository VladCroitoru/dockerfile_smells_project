FROM node:10.15

WORKDIR /app

COPY package.json yarn.lock ./
RUN yarn install && yarn cache clean --force

COPY . .

VOLUME [ "/app" ]

CMD ["yarn", "start"]
