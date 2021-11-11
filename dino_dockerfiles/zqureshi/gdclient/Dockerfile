FROM golang:alpine AS builder
ADD . /go/src/github.com/zqureshi/gdclient
WORKDIR /go/src/github.com/zqureshi/gdclient
RUN apk --no-cache add ca-certificates git && \
  go get github.com/twitchtv/retool && \
  retool sync && \
  retool do dep ensure -v
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /app/gdclient .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
COPY --from=builder /app/* /app/

ENTRYPOINT ["/app/gdclient"]
