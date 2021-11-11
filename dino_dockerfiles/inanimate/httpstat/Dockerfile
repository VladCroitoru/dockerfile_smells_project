FROM golang:1.9 as build
# Note that this pulls from upstream master, not this current repository (inanimate/httpstat)
RUN go get github.com/davecheney/httpstat && \
    CGO_ENABLED=0 GOOS=linux go build github.com/davecheney/httpstat && \
    go test github.com/davecheney/httpstat

FROM alpine:3.7
# This is required for querying https sites
RUN apk --no-cache --update add ca-certificates
COPY --from=build /go/httpstat /
ENTRYPOINT ["/httpstat"]
CMD ["google.com"]
