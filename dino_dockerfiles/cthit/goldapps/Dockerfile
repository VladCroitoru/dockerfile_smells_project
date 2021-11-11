# Dockerfile for goldapps production
FROM golang:1.12-alpine AS buildStage
MAINTAINER digIT <digit@chalmers.it>

# Install git
RUN apk update
RUN apk upgrade
RUN apk add --update git

# Copy sources
RUN mkdir -p /goldapps
COPY . /goldapps
WORKDIR /goldapps/cmd/goldapps

# Grab dependencies
#RUN go get -d -v ./...

# build binary
RUN go install -v
RUN mkdir /app && mv $GOPATH/bin/goldapps /app/goldapps

##########################
#    PRODUCTION STAGE    #
##########################
FROM alpine
MAINTAINER digIT <digit@chalmers.it>

# Add standard certificates
RUN apk update && apk add ca-certificates && rm -rf /var/cache/apk/*

# Set user
RUN addgroup -S app
RUN adduser -S -G app -s /bin/bash app
USER app:app

# Copy execution script
COPY ./sleep_and_run.sh /app/sleep_and_run.sh

# Copy binary
COPY --from=buildStage /app/goldapps /app/goldapps

ENV WAIT 15s

# Set good defaults
WORKDIR /app
ENTRYPOINT ./sleep_and_run.sh
CMD -dry