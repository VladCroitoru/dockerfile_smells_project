# Create image based on my own image or the official Node 6-alpine image from dockerhub
#FROM headcult/angular2starter:dev
FROM node:6.10.0-alpine

# Create a directory where our app will be placed
RUN mkdir -p /usr/src/app

# Change directory so that our commands run inside this new directory
WORKDIR /usr/src/app

# Copy dependency definitions
COPY package.json /usr/src/app/

# Install app dependencies
RUN npm install

# Get all the code needed to run the app
COPY . /usr/src/app

# Expose the port the app runs in
EXPOSE 8080

# Serve the app
CMD [ "npm", "start" ]
