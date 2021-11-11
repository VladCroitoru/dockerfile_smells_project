# Development
FROM golang:1.16-alpine AS development
WORKDIR /go/src/github.com/tidepool-org/clinic
RUN adduser -D tidepool && \
    chown -R tidepool /go/src/github.com/tidepool-org/clinic
USER tidepool
COPY --chown=tidepool . .
RUN ./build.sh
CMD ["./dist/clinic"]
