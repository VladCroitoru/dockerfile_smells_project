FROM node:14.17.4-alpine

ENV NODE_ENV=development

COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "/usr/src/app/"]

WORKDIR /usr/src/app

RUN npm install --also=dev

ADD . .

EXPOSE 5000

CMD ["npm", "run", "dev"]
