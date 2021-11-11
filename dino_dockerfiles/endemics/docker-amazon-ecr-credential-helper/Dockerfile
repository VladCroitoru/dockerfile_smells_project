FROM golang:alpine AS builder
RUN apk --no-cache add git && \
    git clone https://github.com/awslabs/amazon-ecr-credential-helper /go/src/github.com/awslabs/amazon-ecr-credential-helper && \
    go build -o /assets/docker-credential-ecr-login github.com/awslabs/amazon-ecr-credential-helper/ecr-login/cli/docker-credential-ecr-login

FROM alpine:edge AS resource
COPY --from=builder /assets/docker-credential-ecr-login /usr/local/bin/docker-credential-ecr-login
