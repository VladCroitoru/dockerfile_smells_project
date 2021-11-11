###########################################################
#
# Dockerfile for tfk-seneca-skoleskyss-walking-distance
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
ENV TFK_SENECA_SKOLESKYSS_WALKING_DISTANCE_TAG tfk-seneca-skoleskyss-walking-distance
ENV TFK_SENECA_SKOLESKYSS_WALKING_DISTANCE_URL https://skoleskysswalkingdistance.no
ENV TFK_SENECA_SKOLESKYSS_WALKING_DISTANCE_HOST localhost
ENV TFK_SENECA_SKOLESKYSS_WALKING_DISTANCE_PORT 8000
ENV TFK_SENECA_SKOLESKYSS_WALKING_DISTANCE_API_URI https://maps.googleapis.com/maps/api/directions/json
ENV TFK_SENECA_SKOLESKYSS_WALKING_DISTANCE_API_KEY yourapikey

# Startup
CMD ["node", "service.js", "--seneca-log=type:act"]