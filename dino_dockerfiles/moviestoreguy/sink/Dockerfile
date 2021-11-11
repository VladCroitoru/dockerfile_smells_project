FROM golang:1.10-alpine AS GoBuilder

WORKDIR /go/src/github.com/MovieStoreGuy/sink
COPY . .

RUN apk --no-cache add git && \
    go get -v github.com/golang/dep/cmd/dep && \
    dep ensure && \
    CGO_ENABLED=0 GOOS=linux go build -a -installsuffix nocgo -ldflags="-w -s" -o /sink .

FROM scratch

COPY --from=GoBuilder /sink ./

ENTRYPOINT ["./sink"]
ARG ["localhost"]
