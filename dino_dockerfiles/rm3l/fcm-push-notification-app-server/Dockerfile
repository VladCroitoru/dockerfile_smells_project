FROM golang:1.7.1-alpine

#
# Package deps
#
RUN apk add --update build-base
RUN apk add --update git
RUN rm -rf /var/cache/apk/*

#
# Go deps
#
RUN go get -u github.com/caarlos0/env
RUN go get -u github.com/google/go-gcm
RUN go get -u github.com/gorilla/mux
RUN go get -u github.com/rs/cors

#
# Server files
#
RUN mkdir -p /code/server/
ADD . /code/server/
WORKDIR /code/server/

#
# Expose default server port
#
EXPOSE 5000

#
# Run
#
CMD ["go", "run", "server.go"]
