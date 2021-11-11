FROM node:wheezy
MAINTAINER Starfox64 <louisdijon21@yahoo.fr>

COPY package.json /fpauth/
WORKDIR /fpauth

RUN npm install --production

COPY . /fpauth

CMD ["node", "index.js"]
