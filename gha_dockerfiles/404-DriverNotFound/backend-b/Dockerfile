FROM node

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn install

COPY . .

RUN yarn build

EXPOSE 5000

CMD [ "bash", "start.sh" ]
