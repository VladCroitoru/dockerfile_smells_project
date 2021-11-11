FROM node:9.8-alpine
WORKDIR /srv
COPY . /srv
RUN npm install
CMD [ "node", "src/server.js" ]