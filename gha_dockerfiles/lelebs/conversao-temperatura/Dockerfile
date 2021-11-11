FROM node:14
EXPOSE 8080
WORKDIR /app
COPY ./src/package.json .
RUN npm install
COPY ./src .
CMD [ "node", "server.js" ]