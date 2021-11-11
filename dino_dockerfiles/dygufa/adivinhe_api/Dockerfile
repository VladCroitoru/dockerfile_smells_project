FROM node:8.3

WORKDIR /app

COPY package.json /app
COPY yarn.lock /app
RUN yarn install

COPY . /app

EXPOSE 8034
CMD [ "npm", "start" ]