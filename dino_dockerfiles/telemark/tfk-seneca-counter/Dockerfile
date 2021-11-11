###########################################################
#
# Dockerfile for tfk-seneca-counter
#
###########################################################

# Setting the base to nodejs 4.6.1
FROM mhart/alpine-node:4.6.1@sha256:7cdb9fe36a9811d3c77c8c643b57b78fc21ac69c1e1ddda93ca785f82617fbbd

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
ENV TFK_SENECA_COUNTER_TAG tfk-seneca-counter
ENV TFK_SENECA_COUNTER_FIREBASE_URL https://seneca-firebase-test.firebaseio.com
ENV TFK_SENECA_COUNTER_FIREBASE_API_KEY firebase-api-key
ENV TFK_SENECA_COUNTER_HOST localhost
ENV TFK_SENECA_COUNTER_PORT 8000

# Startup
CMD ["node", "service.js", "--seneca-log=type:act"]