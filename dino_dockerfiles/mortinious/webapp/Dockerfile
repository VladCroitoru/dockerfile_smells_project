# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang:1.8.3-jessie

# Copy the local package files to the container's workspace and create dirs
RUN  mkdir -p /go/src \
  && mkdir -p /go/bin \
  && mkdir -p /go/pkg
ENV GOPATH=/go
ENV PATH=$GOPATH/bin:$PATH

RUN mkdir -p $GOPATH/src/webapp
ADD . /go/src/webapp


# Install godep for later use
RUN go get github.com/tools/godep


# Build the app command inside the container.
#RUN go get github.com/gorilla/securecookie \
#	&& go get github.com/gorilla/context \
#	&& go get github.com/gorilla/sessions
#RUN cd $GOPATH/src/webapp && godep save && godep go build

RUN cd $GOPATH/src/webapp && godep go build

# Run the app command by default when the container starts.
ENTRYPOINT /go/src/webapp/webapp


# Document that the service listens on port 7001.
EXPOSE 7001