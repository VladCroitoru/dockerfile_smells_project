FROM node:boron

# Create app directory
ADD . /app
WORKDIR /app

# Install app dependencies
COPY package.json /usr/src/app/
RUN npm install
RUN npm install webpack -g

# Bundle app source
COPY . /usr/src/app
