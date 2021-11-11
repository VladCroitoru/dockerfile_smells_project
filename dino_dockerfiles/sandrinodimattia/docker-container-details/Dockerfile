FROM mhart/alpine-node:6.2

WORKDIR /usr/src/

COPY package.json .
RUN npm install

COPY . .

ENTRYPOINT ["node", "/usr/src/server.js"]
