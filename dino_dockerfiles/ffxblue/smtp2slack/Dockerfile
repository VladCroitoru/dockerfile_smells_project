FROM node:6
MAINTAINER 3846masa

WORKDIR /usr/src/app

COPY package.json package.json
RUN npm i
COPY . .

EXPOSE 25
CMD ["node", "index.js"]
