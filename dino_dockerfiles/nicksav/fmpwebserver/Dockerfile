# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

# Copy the local package files to the container's workspace.
ADD . /go/src/fmpwebserver

ENV GO_ENV production

# Build the outyet command inside the container.
# (You may fetch or manage dependencies here,
# either manually or with a tool like "godep".)
RUN go get github.com/dgrijalva/jwt-go
RUN go get github.com/go-sql-driver/mysql
RUN go get gopkg.in/gomail.v2
RUN go get github.com/gorilla/context
RUN go get github.com/urfave/negroni
RUN go get github.com/garyburd/redigo/redis
RUN go get github.com/gorilla/mux
RUN go get golang.org/x/crypto/bcrypt
RUN go install fmpwebserver


ADD settings /go/bin/settings

# Run the outyet command by default when the container starts.
ENTRYPOINT /go/bin/fmpwebserver

# Document that the service listens on port 8080.
EXPOSE 5000
