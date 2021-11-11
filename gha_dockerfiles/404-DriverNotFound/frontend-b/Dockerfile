FROM node

WORKDIR /app

COPY package.json yarn.lock ./

RUN yarn --silent
RUN yarn add serve

COPY . .

RUN yarn build

EXPOSE 3000

#CMD [ "yarn", "start" ]
CMD ["yarn", "serve", "-s", "build", "-l", "3000"]
