# Use a base image
FROM node:alpine

# Create a workdir
RUN mkdir -p /app
WORKDIR /app

# Install npm packages
COPY package.json /app
RUN npm install