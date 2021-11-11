FROM node:12

# Create app directory
WORKDIR /usr/src/webserver

COPY package*.json ./
RUN npm install

COPY ./*.js ./

EXPOSE 3000

CMD [ "node", "webserver.js", "--redirectUri", "http://localhost:58816/ext-core-webapi/callback/LocalOAuth", "--refreshTokenLifetimeSeconds", "45", "--accessTokenLifetimeSeconds", "20" ]