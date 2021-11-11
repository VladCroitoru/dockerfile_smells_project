FROM node:8.0

ENV NODE_ENV production

EXPOSE 80
EXPOSE 443
EXPOSE 3978

WORKDIR /usr/src/app

COPY ["package.json", "npm-shrinkwrap.json*", "./"]

RUN npm install --production --silent

COPY . .

CMD npm start