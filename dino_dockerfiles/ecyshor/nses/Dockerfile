FROM golang:1 as build
RUN apt update && apt install unzip
RUN curl -OL https://github.com/google/protobuf/releases/download/v3.4.0/protoc-3.4.0-linux-x86_64.zip && \
    unzip protoc-3.4.0-linux-x86_64.zip -d protoc3 && \
    mv protoc3/bin/* /usr/local/bin/ && \
    mv protoc3/include/* /usr/local/include/ && \
    ln -s /protoc3/bin/protoc /usr/bin/protoc

WORKDIR /go/src/github.com/ecyshor/nses
RUN go get -u github.com/golang/protobuf/protoc-gen-go
COPY . .
RUN protoc --go_out=plugins=grpc:. *.proto
RUN go get -d -v
RUN go install -v
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o nses .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=build /go/src/github.com/ecyshor/nses/nses .
COPY migrations migrations
EXPOSE 8000
CMD ["/root/nses"]