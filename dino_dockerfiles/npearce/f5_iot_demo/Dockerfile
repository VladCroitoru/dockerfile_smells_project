############################################################
# Dockerfile to build Super-NetOps enablement container
# Based on Alpine Linux, seasoned with tools and workflows
############################################################

# Start with an awesome, tiny Linux distro.
FROM alpine:latest

MAINTAINER Nathan Pearce

ENV REPO_RAW https://raw.githubusercontent.com/npearce/f5_iot_demo/master
ENV LOCAL_PATH /f5_iot_demo

# Update the Alpine package database
RUN apk update

# Install Node.js
RUN apk add nodejs

ADD $REPO_RAW/iot_client_inputs.json $LOCAL_PATH/
ADD $REPO_RAW/iot_client.js $LOCAL_PATH/
ADD $REPO_RAW/iot_client-nofilter.js $LOCAL_PATH/
ADD $REPO_RAW/iot_client-noselect.js $LOCAL_PATH/
ADD $REPO_RAW/iot_client-rjd_8100.js $LOCAL_PATH/

# CMD /usr/bin/node $LOCAL_PATH/iot_client.js
