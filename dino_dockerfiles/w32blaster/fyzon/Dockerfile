#
#
# Stage 1: Build Semantic theme using NPM
#
# We use official NODE image to build the  Semantic UI using NPM and pass it to runtime container
#
FROM node:alpine AS semantic-builder

ADD . /go/src/github.com/w32blaster/fyzon

RUN cd /go/src/github.com/w32blaster/fyzon && \

    # Build the Semantic UI and gulp
    npm install && \
    npm install semantic-ui --save && \
    npm install gulp -g && \

    # Build current theme for our Fyzon using gulp
    cd semantic && \
    gulp build

#
#
# Stage 2: build the production image
#
FROM golang:1.7-alpine

ADD . /go/src/github.com/w32blaster/fyzon
COPY --from=semantic-builder /go/src/github.com/w32blaster/fyzon/semantic /go/bin/semantic

# add templates to the WORKDIR
ADD ./templates /go/bin/templates
ADD ./assets /go/bin/assets

# install SQlite3 to set up a new database
RUN apk add --no-cache sqlite && \
    mkdir -p /go/bin/db && \

    # install database to the WORKDIR
    sqlite3 /go/bin/db/trans.sqlite3 < src/github.com/w32blaster/fyzon/db/schema.sql && \
    cp src/github.com/w32blaster/fyzon/db/schema.sql /go/bin/ && \

    # copy DB import script for those folks who might want to keep database outside of the container
    cp src/github.com/w32blaster/fyzon/db/importDb.sh /go/bin/ && \
    chmod +x /go/bin/importDb.sh

RUN set -ex && \
    apk add --no-cache git gcc g++
    

RUN cd /go/src/github.com/w32blaster/fyzon && \
    go get -u -v github.com/kardianos/govendor && \
    
    # install dependencies    
    govendor fetch -v +out  && \

    # build the project
    CGO_ENABLED=0 go build -a -installsuffix cgo --ldflags="-s" && \
    go install . && \

    # remove git and nodeJS, because we don't need it at runtime
    apk del git && \
    rm -rf /var/cache/apk/* && \

    # remove sources as well, because we already compiled at the moment and we don't need them on runtime
    rm -rf /go/src

ENV GIN_MODE=release

WORKDIR /go/bin

VOLUME /go/bin/db
EXPOSE 8080

ENTRYPOINT /go/bin/fyzon
