FROM golang:1.15 as builder
WORKDIR /go/src/github.com/proofpoint/kubernetes-ldap/

COPY . .
RUN go test -mod=vendor ./...
RUN CGO_ENABLED=0 GOOS=linux go build -mod=vendor --ldflags "-s -w" -o bin/kubernetes-ldap .

FROM alpine:3.12.0
## use https
RUN sed -i 's/http\:\/\//https\:\/\//g' /etc/apk/repositories
RUN apk add --no-cache ca-certificates
WORKDIR /opt/
COPY --from=builder /go/src/github.com/proofpoint/kubernetes-ldap/bin/kubernetes-ldap .
ENTRYPOINT ["./kubernetes-ldap"]
