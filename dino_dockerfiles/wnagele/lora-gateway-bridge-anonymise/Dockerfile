FROM node

WORKDIR /home/node/app/
ADD package.json /home/node/app/
RUN npm install

ADD server.js /home/node/app/
CMD npm start
