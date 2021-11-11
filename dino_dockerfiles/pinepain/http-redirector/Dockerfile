FROM golang:1.10 AS build

# Cd into the api code directory
WORKDIR /go/src/github.com/pinepain/http-redirector

# Copy the local package files to the container's workspace.
ADD . /go/src/github.com/pinepain/http-redirector

RUN CGO_ENABLED=0 GOOS=linux go build \
    && go test -cover


FROM scratch
COPY --from=build /go/src/github.com/pinepain/http-redirector /

ENTRYPOINT ["/http-redirector"]