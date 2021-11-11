# Build
FROM golang:1.9-alpine3.6 as builder
RUN apk update && apk add git
RUN go get -u github.com/Masterminds/glide
ADD . /go/src/lag-api
WORKDIR /go/src/lag-api
RUN glide install
RUN CGO_ENABLED=0 GOOS=linux go build -ldflags "-s" -a -installsuffix cgo -o /lag-api .
ENTRYPOINT ["/bin/true"]

# Release
FROM alpine:3.6
COPY --from=builder /lag-api /lag-api
ENTRYPOINT ["/lag-api"]
