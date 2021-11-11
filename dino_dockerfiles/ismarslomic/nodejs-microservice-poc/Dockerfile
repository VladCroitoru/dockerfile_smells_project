# Set the base image to mongo
FROM    node:latest

# File Author / Maintainer
MAINTAINER Ismar Slomic <ismar@slomic.no>

# Define working directory
WORKDIR /opt

# Install curl, git, nodejs and npm
RUN apt-get update && apt-get install -y \
    git \
    curl
RUN curl -sL https://deb.nodesource.com/setup_0.12 | bash -
RUN apt-get update && apt-get install -y nodejs

# Clone nodejs-microservice-poc from Github (the rest api)
RUN git clone https://github.com/ismarslomic/nodejs-microservice-poc.git

# Navigate to the nodejs-microservice-poc folder
WORKDIR nodejs-microservice-poc

# Install NPM dependencies
RUN npm install

# Expose port 3000 for nodejs-microservice-poc
EXPOSE  3000

# Start the application in nodejs
CMD npm start
