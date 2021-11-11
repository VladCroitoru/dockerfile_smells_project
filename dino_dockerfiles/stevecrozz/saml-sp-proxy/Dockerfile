FROM golang:1.10 AS builder
ADD https://github.com/golang/dep/releases/download/v0.4.1/dep-linux-amd64 /usr/bin/dep
RUN chmod +x /usr/bin/dep
WORKDIR $GOPATH/src/github.com/username/repo
COPY Gopkg.toml Gopkg.lock ./
RUN dep ensure --vendor-only
COPY . ./
RUN CGO_ENABLED=0 GOOS=linux go build -o /bin/entrypoint .

FROM scratch
COPY --from=builder /bin/entrypoint /bin/entrypoint
EXPOSE 8080/tcp
ENTRYPOINT ["/bin/entrypoint"]
