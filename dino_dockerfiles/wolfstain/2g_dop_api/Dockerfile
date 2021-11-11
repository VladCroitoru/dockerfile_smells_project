FROM node:carbon-slim

# Create app directory
WORKDIR /git/dop-api

# Install app dependencies
COPY package.json /git/dop-api/
RUN npm install

# Bundle app source
COPY . /git/dop-api/
RUN npm run prepublish

CMD [ "npm", "run", "runServer" ]