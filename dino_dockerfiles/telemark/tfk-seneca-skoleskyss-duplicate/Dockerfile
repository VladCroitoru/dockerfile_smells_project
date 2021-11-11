###########################################################
#
# Dockerfile for tfk-seneca-skoleskyss-duplicate
#
###########################################################

# Setting the base to nodejs 4.6.0
FROM mhart/alpine-node:4.6.0

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
ENV TFK_SENECA_SKOLESKYSS_DUPLICATE_TAG tfk-seneca-skoleskyss-duplicate
ENV TFK_SENECA_SKOLESKYSS_DUPLICATE_URL https://skoleskyssduplicates.no
ENV TFK_SENECA_SKOLESKYSS_DUPLICATE_HOST localhost
ENV TFK_SENECA_SKOLESKYSS_DUPLICATE_PORT 8000
ENV TFK_SENECA_SKOLESKYSS_DUPLICATE_MONGODB_URI mongodb://localhost/duplicate

# Startup
CMD ["node", "service.js", "--seneca-log=type:act"]