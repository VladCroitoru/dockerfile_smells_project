# ### Build stage
FROM golang:1.13.5 as builder
WORKDIR /go/src/project
ARG SSH_PRIVATE_KEY

# Install certificates for using SSL
RUN apt-get install ca-certificates

# Get sources and build app
WORKDIR /go/src/project
COPY . .
RUN go mod download
#RUN go test -v -cover *.go
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -o app *.go

# ### Run stage
FROM scratch
COPY --from=builder /etc/ssl/ /etc/ssl/
COPY --from=builder /go/src/project/app /app
ENTRYPOINT ["/app"]
