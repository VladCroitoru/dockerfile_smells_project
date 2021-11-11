FROM node:7.7.3

MAINTAINER Gustav Karlsson

# Install node applications
RUN npm install -g gulp http-server

# Work in app directory
WORKDIR /app

# Add package.json for installing project dependencies
ADD package.json /app/package.json

# Install project dependencies
RUN npm install

# Add remaining source files
ADD . /app

# Build project
RUN gulp --production

# Application will listen on this port number
EXPOSE 8080

# Run server
CMD http-server -p 8080 -d False build
