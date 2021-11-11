###########################################################
#
# Dockerfile for utdaterte-artikler
#
###########################################################

# Setting the base to nodejs 4.8.0
FROM node:4.8.0-alpine

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
RUN npm install

# Env variables
ENV SERVER_PORT 3000
ENV BASE_URL https://www.telemark.no
ENV SITEMAP_URL https://www.telemark.no/sitemap.xml
ENV YAR_SECRET passwordpasswordpasswordpassword

# Expose 3000
EXPOSE 3000

# Startup
ENTRYPOINT node standalone.js