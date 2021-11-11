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

# Clone mongo-express from Github (mongodb GUI)
RUN git clone https://github.com/ismarslomic/mongo-express.git

# Navigate to the mongo-express folder
WORKDIR mongo-express

# Install NPM dependencies
RUN npm install

# Expose port 8081 for mongo-express
EXPOSE  8081

# Start the application in nodejs
CMD npm start