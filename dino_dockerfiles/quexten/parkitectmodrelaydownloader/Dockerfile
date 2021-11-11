FROM node:carbon
# Create app directory
WORKDIR /usr/src/app

COPY package*.json ./
RUN yarn install
RUN apt-get update
RUN apt-get install lib32gcc1 -y
# Bundle app source
COPY . .
EXPOSE 80
CMD [ "npm", "start" ]
