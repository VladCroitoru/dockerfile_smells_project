FROM node:4-onbuild

WORKDIR /usr/src/app

COPY package.json /usr/src/app
RUN npm install

COPY . /usr/src/app

EXPOSE 28469

CMD [ "npm", "start" ]
CMD [ "node", "index.js" ]
