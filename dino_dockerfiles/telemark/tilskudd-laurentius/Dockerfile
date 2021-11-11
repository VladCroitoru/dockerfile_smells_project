# Setting the base to nodejs 8.6.0
FROM node:8.16.0-alpine@sha256:9e818f25afa9c9155a7d129dc23a695c6abda23f218888584924987149a37db0

# Maintainer
MAINTAINER Geir Gåsodden

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
ENTRYPOINT node example.js
