FROM node

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
COPY app.js /usr/src/app/

RUN npm install -g nodemon
RUN npm install

EXPOSE 3000
CMD [ "npm", "start" ]