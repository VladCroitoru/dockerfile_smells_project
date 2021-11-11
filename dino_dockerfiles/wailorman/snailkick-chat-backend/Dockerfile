FROM node:latest
MAINTAINER wailorman

RUN mkdir /snail
ADD . /snail
WORKDIR /snail
RUN npm install

EXPOSE 27017
EXPOSE 1515:1515

CMD ["node", "oauth-test.js"]