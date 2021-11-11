FROM golang:latest as builder
WORKDIR /go/src/github.com/leonidboykov/docker-whoami
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o whoami .

FROM scratch
COPY --from=builder /go/src/github.com/leonidboykov/docker-whoami/whoami /
EXPOSE 8080
ENTRYPOINT ["/whoami"]
