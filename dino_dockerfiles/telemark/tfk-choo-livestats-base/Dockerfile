###########################################################
#
# Dockerfile for Dockerhub-webhook
#
###########################################################

# Setting the base to nodejs 6
FROM mhart/alpine-node:6@sha256:a45e14794a649a5f99bf5677c28ad711d8d0dd7311f79c32266a90214d3e34ad

# Maintainer
MAINTAINER Geir Gåsodden

#### Begin setup ####

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Env variables
ENV SERVER_PORT 3000
ENV LIVESTATS_DB_URL https://tfk-stats.firebaseio.com
ENV LIVESTATS_ENTRYPOINT tilskudd
ENV LIVESTATS_APP_TITLE Livestatistikk tilskudd.t-fk.no

# Install dependencies
RUN npm install
RUN npm run build
RUN npm install -g list

# Expose 3000
EXPOSE 3000

# Startup
ENTRYPOINT list /src/dist
