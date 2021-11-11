FROM golang as builder
WORKDIR /go/src/github.com/jobteaser/kubectl-oidc-helper
RUN go get -u github.com/golang/dep/cmd/dep
COPY . /go/src/github.com/jobteaser/kubectl-oidc-helper
RUN dep ensure && \
    CGO_ENABLED=0 GOOS=linux go build -o kubectl-oidc-helper . 

FROM alpine:3.6
RUN apk --no-cache add ca-certificates && update-ca-certificates
COPY --from=builder /go/src/github.com/jobteaser/kubectl-oidc-helper/kubectl-oidc-helper /kubectl-oidc-helper
ENTRYPOINT [ "/kubectl-oidc-helper" ]