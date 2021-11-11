###########################################################
#
# Dockerfile for tfk-seneca-base
#
###########################################################

# Setting the base to nodejs 4.7.0
FROM mhart/alpine-node:4.7.0@sha256:7db1a86b88e1953b1c61ac2f97df7957a49b1cfe084709ba98cddea895d7f99d

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

# Env variables
ENV TFK_SENECA_BASE_TAG tfk-seneca-base

# Startup
CMD ["node", "service.js", "--seneca-log=type:act"]