# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

RUN apt-get update && apt-get install mc mongodb --yes

# Copy the local package files to the container's workspace.
ADD . /go/src/github.com/RoflCopter24/citation-db

# Build the outyet command inside the container.
# (You may fetch or manage dependencies here,
# either manually or with a tool like "godep".)
RUN go get golang.org/x/crypto/bcrypt
RUN go get gopkg.in/mgo.v2
RUN go get gopkg.in/mgo.v2/bson
RUN go get github.com/gorilla/context
RUN go get github.com/RoflCopter24/negroni-sessions
RUN go get github.com/RoflCopter24/negroni-sessions/cookiestore
RUN go install github.com/RoflCopter24/citation-db

RUN mv /go/src/github.com/RoflCopter24/citation-db/html /srv/html
RUN mv /go/src/github.com/RoflCopter24/citation-db/public /srv/public

ENV MONGO_DB 127.0.0.1
ENV MONGO_DB_PORT 27017
ENV WORKINGDIR /srv

VOLUME /var/lib/mongodb/db
VOLUME /var/uploads

#RUN systemctl enable mongodb.service
#RUN service mongodb start

# Run the outyet command by default when the container starts.
ENTRYPOINT /go/bin/citation-db

# Document that the service listens on port 8080.
EXPOSE 8080
