###########################################################
#
# Dockerfile for louie-web
#
###########################################################

# Setting the base to nodejs 4.2.4
FROM mhart/alpine-node:4.2.4

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

# Expose 3000
EXPOSE 3000

# Startup
ENTRYPOINT node standalone.js