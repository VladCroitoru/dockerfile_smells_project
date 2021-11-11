# Dockerfile for EatIT in production
FROM debian:jessie AS buildStage
MAINTAINER digIT <digit@chalmers.it>

ENV METEOR_VERSION 1.6.1

# Setup directories and user
RUN mkdir /app && mkdir /output && \
    groupadd -r meteor && useradd -m -g meteor meteor
WORKDIR /app

# Install prerequisites
RUN apt-get update && apt-get install -y \
    curl git

# Copy Source files
COPY . .

# Change ownership and su unprivileged user
RUN chown -R meteor:meteor /app && chown -R meteor /output
USER meteor:meteor

# Install meteor
RUN curl https://install.meteor.com/?release=$METEOR_VERSION | sh
USER root:root
RUN cp /home/meteor/.meteor/packages/meteor-tool/$METEOR_VERSION/mt-os.linux.x86_64/scripts/admin/launch-meteor /usr/bin/meteor
USER meteor:meteor

# Build and extract app
RUN meteor npm install
RUN meteor build /output
WORKDIR /output
RUN tar -zxf app.tar.gz && rm app.tar.gz


##########################
#    PRODUCTION STAGE    #
##########################
FROM node:9.1.0 AS production
MAINTAINER digIT <digit@chalmers.it>

# Build arguments
ARG port=8080

# Copy files from the build stage
COPY --from=buildStage /output /app

# Setup and su as unprivileged user
RUN chown -R node:node /app
USER node:node

# Install the application
WORKDIR /app/bundle/programs/server
RUN npm install

# Setup environment
ENV MONGO_URL mongodb://user:password@host:port/databasename
ENV ROOT_URL https://example.com
ENV MAIL_URL smtp://user:password@mailhost:port
ENV PORT $port
EXPOSE $port

# Provide default command and entrypoint
WORKDIR /app/bundle
CMD node main.js
