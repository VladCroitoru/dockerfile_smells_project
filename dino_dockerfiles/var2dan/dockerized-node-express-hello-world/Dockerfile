FROM node:8-alpine

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package.json ./
RUN npm install

COPY . .

# replace this with your application's default port
EXPOSE 3000

CMD [ "npm", "start" ]
