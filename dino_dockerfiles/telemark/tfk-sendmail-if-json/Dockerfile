###########################################################
#
# Dockerfile for tfk-sendmail-if-json
#
###########################################################

# Setting the base to nodejs 4.6.2
FROM mhart/alpine-node:4.6.2

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