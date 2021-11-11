# Setting the base to nodejs 8.11.1
FROM node:8.17.0-alpine@sha256:c8456a06563920080bdc01715626c1be8211edc8cd18f34f15e1b7b936e30746

#### Begin setup ####

# Installs git
RUN apk add --update git && rm -rf /var/cache/apk/*

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Startup
ENTRYPOINT node cli.js --dataset=$DATASET --query=$QUERY --format=$FORMAT