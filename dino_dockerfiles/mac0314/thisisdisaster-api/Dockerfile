# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

# Copy the local package files to the container's workspace.
ADD . /go/src/ThisIsDisaster-API

# Install revel and the revel CLI.
RUN go get github.com/revel/revel
RUN go get github.com/revel/cmd/revel
RUN go get github.com/revel/cron
RUN go get github.com/go-gorp/gorp
RUN go get github.com/go-sql-driver/mysql
RUN go get github.com/go-redis/redis
RUN go get firebase.google.com/go
RUN go get google.golang.org/api/option
RUN go get golang.org/x/crypto/bcrypt
RUN go get golang.org/x/oauth2

# Use the revel CLI to start up our application.
ENTRYPOINT revel run ThisIsDisaster-API dev 9000

# Open up the port where the app is running.
EXPOSE 9000
