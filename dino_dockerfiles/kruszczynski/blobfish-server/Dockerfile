FROM nanoservice/go:latest

# Create app directory.
RUN go get "github.com/gorilla/mux"
RUN go get "github.com/boltdb/bolt"
ENV APP_HOME=${GOPATH}/src/github.com/happyblobfish/server
RUN mkdir -p $APP_HOME
VOLUME ${APP_HOME}/db
WORKDIR $APP_HOME
ADD . $APP_HOME

# Build dependencies and the ws binary
RUN go build
