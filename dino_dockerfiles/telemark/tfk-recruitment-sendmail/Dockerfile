###########################################################
#
# Dockerfile for tfk-recruitment-sendmail
#
###########################################################

# Setting the base to nodejs 7.5.0
FROM node:7.5.0-alpine

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
ENTRYPOINT node example
