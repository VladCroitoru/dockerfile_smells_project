###########################################################
#
# Dockerfile for tilskudd.t-fk.no
#
###########################################################

# Setting the base to nodejs 4.6.2
FROM mhart/alpine-node:4.6.2

# Maintainer
MAINTAINER Geir Gåsodden

#### Begin setup ####

# Installs git
RUN apk add --update --no-cache git

# Extra tools for native dependencies
RUN apk add --no-cache make gcc g++ python

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

EXPOSE 8000

# Startup
ENTRYPOINT node standalone.js