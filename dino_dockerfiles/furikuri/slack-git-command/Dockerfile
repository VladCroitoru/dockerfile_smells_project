FROM node:argon

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
COPY index.js /usr/src/app/
COPY lib /usr/src/app/
RUN npm install

EXPOSE 8080

CMD [ "npm", "start" ]