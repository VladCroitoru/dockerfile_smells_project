FROM node:9.4
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3101
CMD [ "npm", "start" ]