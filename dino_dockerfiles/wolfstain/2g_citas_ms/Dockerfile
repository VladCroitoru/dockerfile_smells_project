# golang image where workspace (GOPATH) configured at /go.
FROM golang:1.10

# Install dependencies
RUN go get github.com/gorilla/mux
RUN go get gopkg.in/mgo.v2
RUN go get github.com/night-codes/mgo-ai

# copy the local package files to the container workspace
COPY . /go/src/2g_citas_ms

# Build the users command inside the container.
RUN go install 2g_citas_ms

# Run the users microservice when the container starts.
ENTRYPOINT /go/bin/2g_citas_ms

# Service listens on port 3300.
EXPOSE 4002
