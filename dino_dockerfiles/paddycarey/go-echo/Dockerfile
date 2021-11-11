FROM golang:1.6.0-alpine

# Expose HTTP port and set necessary environment variables
EXPOSE 8000

# copy source code into the $GOPATH and switch to that directory
COPY . ${GOPATH}/src/github.com/shopkeep/go-echo
WORKDIR ${GOPATH}/src/github.com/shopkeep/go-echo

# compile source code and copy into $PATH
RUN go install

# the default command runs the service in the foreground
CMD ["go-echo"]
