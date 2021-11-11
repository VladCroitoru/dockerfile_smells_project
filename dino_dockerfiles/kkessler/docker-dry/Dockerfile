FROM golang:1.6.0-alpine

# create folder
RUN mkdir -p /go/src/app
WORKDIR /go/src/app

# get dependancies
RUN apk update && apk add curl file

# install dry
RUN curl -sSf https://moncho.github.io/dry/dryup.sh | sh
RUN chmod 755 /usr/local/bin/dry
CMD ["/usr/local/bin/dry"]
