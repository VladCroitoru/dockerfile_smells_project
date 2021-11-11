###########################################################
#
# Dockerfile for politikk.microsite.t-fk.no
#
###########################################################

# Setting the base to nodejs 4.6.0
FROM mhart/alpine-node:4.9.1@sha256:052772af605978749631e2b6d190c7d68dc607a480a6e4dbe84eaf7264759d2e

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

# Env variables
ENV OPENGOV_MEETINGS_API_URL https://opengov.api.t-fk.no
ENV OPENGOV_POLITICIANS_API_URL https://politiker-api.t-fk.no
ENV OPENGOV_SEARCH_API_URL https://politics.search.t-fk.no
ENV OPENGOV_POLITIKK_SERVER_PORT 8000

EXPOSE 8000

# Startup
ENTRYPOINT node standalone.js