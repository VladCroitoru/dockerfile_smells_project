###########################################################
#
# Dockerfile for micro-status-saksbehandling-skoleskyss
#
###########################################################

# Setting the base to nodejs 7.4.0
FROM node:7.4.0-alpine

# Maintainer
MAINTAINER Geir Gåsodden

#### Begin setup ####

# Installs git
RUN apk add --update --no-cache git

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

ENV NODE_ENV production

# Expose 8080
EXPOSE 8080

# Startup
ENTRYPOINT npm start