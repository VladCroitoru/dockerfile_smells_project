FROM mhart/alpine-node:slim-12

# Set newman version 
ENV NEWMAN_VERSION 5.3.0

RUN apk update \
    && apk upgrade \
    && apk add openjdk8 bash \
    && npm install newman --global \
    && rm -rf /var/cache/apk/*
    
# Install newman
RUN npm install -g newman@${NEWMAN_VERSION};
