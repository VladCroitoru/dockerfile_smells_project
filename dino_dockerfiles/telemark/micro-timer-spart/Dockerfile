###########################################################
#
# Dockerfile for micro-timer-start
#
###########################################################

# Setting the base to nodejs 7.5.0
FROM node:7.10.1-alpine

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

# Expose 8080
EXPOSE 8080

# Startup
ENTRYPOINT npm start