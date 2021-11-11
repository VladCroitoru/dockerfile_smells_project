# We build from an official Node image from Docker
FROM node:12.10.0

# Create app directory
# This will create /app folder inside the image
# Everything from here will be copied to /app
WORKDIR /app

# Copy package files
# A wildcard is used to ensure both package.json AND package-lock.json are copied
COPY package*.json ./
COPY client/package*.json ./client/

# Install all dependencies
# This will create node_modules folders inside docker image
RUN npm install
RUN npm run install:client

# Copy our source code into the image
COPY . ./

# Build the client side code from react-scripts
RUN npm run build:client

#Expose the port that our Node Express server will run
EXPOSE 5001

# Define the runtime command
# This will execute when we run our docker image
CMD ["node", "server.js"]