# Stage 0 - Build
FROM golang:1.10.0-alpine AS build

ENV PACKAGE=github.com/mendsley/parchment

ADD . /go/src/${PACKAGE}

RUN go vet ${PACKAGE}/...
RUN go test ${PACKAGE}/...
RUN go install -v -tags netgo ${PACKAGE} ${PACKAGE}/...

# Stage 1 - Final image
FROM alpine:3.7
LABEL maintainer="Matthew Endsley <mendsley@gmail.com>"

COPY --from=build /go/bin/parchment /go/bin/parchment-cat /go/bin/parchment-journald /usr/bin/
