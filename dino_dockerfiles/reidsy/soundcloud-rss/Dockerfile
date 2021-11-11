FROM golang:1.13 as build
WORKDIR /go/src/github.com/reidsy/soundcloud-rss/
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GO111MODULE=on go build -a .
RUN echo "go:*:10001:10001:Go application user:/go:" > ./passwd

FROM scratch
ARG GIT_COMMIT=UNKNOWN
LABEL git-commit=$GIT_COMMIT
COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
COPY --from=build /go/src/github.com/reidsy/soundcloud-rss/passwd /etc/passwd
COPY --from=build /go/src/github.com/reidsy/soundcloud-rss/soundcloud-rss /go/bin/soundcloud-rss
USER go
ENTRYPOINT ["/go/bin/soundcloud-rss"]
EXPOSE 8080
