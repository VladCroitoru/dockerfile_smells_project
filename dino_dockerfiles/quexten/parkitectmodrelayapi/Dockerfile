FROM node:carbon
# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./
RUN yarn
# Bundle app source
COPY . .
EXPOSE 8080

CMD [ "npm", "start" ]
