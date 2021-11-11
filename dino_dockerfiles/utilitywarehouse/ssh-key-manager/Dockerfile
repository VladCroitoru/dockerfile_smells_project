FROM golang:1.16-alpine AS build
WORKDIR /go/src/github.com/utilitywarehouse/ssh-key-manager
COPY . /go/src/github.com/utilitywarehouse/ssh-key-manager
RUN apk --no-cache add git gcc musl-dev \
 && go get ./... \
 && go test -v \
 && CGO_ENABLED=0 go build -o /ssh-key-manager .

FROM alpine:3.14
RUN apk add --no-cache ca-certificates
COPY --from=build /ssh-key-manager /ssh-key-manager
CMD [ "/ssh-key-manager" ]
