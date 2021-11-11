FROM node:14

WORKDIR /usr/src/

COPY package.json ./
COPY yarn.lock ./

RUN yarn install

COPY . .

EXPOSE 6006

CMD ["yarn", "start"]