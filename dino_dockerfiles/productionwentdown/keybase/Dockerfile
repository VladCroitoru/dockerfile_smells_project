#
# Build stage
#
FROM golang:1.12-alpine as builder

# deps
RUN apk --no-cache add git build-base

# get and install
RUN go get -v github.com/keybase/client/go/keybase
RUN go install -v --ldflags '-extldflags "-static"' -tags production github.com/keybase/client/go/keybase


#
# Final image
#
FROM scratch

# labels
LABEL org.label-schema.vcs-url="https://github.com/productionwentdown/keybase"
LABEL org.label-schema.version=${version}
LABEL org.label-schema.schema-version="1.0"

# copy ca-certs
COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

# copy keybase binary
COPY --from=builder /go/bin/keybase /keybase

ENTRYPOINT ["/keybase", "--standalone"]
CMD ["version"]
