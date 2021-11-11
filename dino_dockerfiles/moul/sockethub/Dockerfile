FROM node:10
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
RUN mkdir -p log && chmod 777 log
EXPOSE 3000
CMD [ "node", "app.js" ]