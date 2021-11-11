###########################################################
#
# Dockerfile for tfk-seneca-mesh-counter
#
###########################################################

# Setting the base to nodejs 4.6.2
FROM mhart/alpine-node:4.6.2@sha256:256155fa2a149cbf935529979113a0c93286f4acb9cf9516c052065681813aa5

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

# Startup
CMD ["node", "service.js", "--seneca-log=type:act"]