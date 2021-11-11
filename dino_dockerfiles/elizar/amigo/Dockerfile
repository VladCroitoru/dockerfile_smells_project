FROM golang:1.13
COPY . /amigo
WORKDIR /amigo
RUN CC=$(which musl-gcc) go build --ldflags '-w -linkmode external -extldflags "-static"' -o amigo main.go

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /amigo
COPY --from=0 /amigo /amigo
CMD ["./amigo"]

