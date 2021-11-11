FROM node:8
WORKDIR /opt/wallabot
COPY package*.json /opt/wallabot/
RUN npm install
COPY . /opt/wallabot/
CMD node app.js
