# Install 'dep' from golang/dep on an Golang image
# Then copy it into a base Alpine image
FROM golang:alpine AS build

# Build golang 'dep'
RUN apk update
RUN apk add git
RUN go get -u github.com/golang/dep/cmd/dep

# Create final image
FROM alpine

RUN apk update && apk add git 
COPY --from=build /go/bin/dep /usr/local/bin/dep

ENTRYPOINT ["dep"]

