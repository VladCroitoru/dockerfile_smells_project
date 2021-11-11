FROM golang:1.9-alpine
MAINTAINER Joel Stephens https://github.com/jbstep
LABEL authors="Gabriel Alacchi: alacchi.g@gmail.com, Christian Muehlhaeuser: muesli@gmail.com, Henry Wang: henry@wangqiru.com"

# URL has to be set to the URL of Beehive administrator interface
ENV URL=http://localhost:8181

# Install dependencies and beehive
RUN apk add --no-cache git build-base --no-cache && \
    rm -rf /var/cache/apk/* &&\ 
    go get github.com/muesli/beehive
    
# Set the working directory for the container
WORKDIR /go/src/github.com/muesli/beehive

# create a volume for the configuration persistence
VOLUME /conf

# Expose the application port
EXPOSE 8181

ENTRYPOINT beehive -config /conf/beehive.conf -bind 0.0.0.0:8181 -canonicalurl ${URL}
