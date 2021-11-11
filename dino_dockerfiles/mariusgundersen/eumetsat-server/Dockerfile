FROM node:10

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install --silent && npm cache clean --force
COPY . /usr/src/app
ENV NODE_ENV production

CMD [ "npm", "start" ]

EXPOSE 8080