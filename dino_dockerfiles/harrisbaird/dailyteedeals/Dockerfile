# Build binary
FROM golang:alpine AS build-env
LABEL maintainer "daniel@harrisbaird.co.uk"
RUN apk --update --no-cache add git make
WORKDIR /go/src/github.com/harrisbaird/dailyteedeals
ADD . .
RUN make install && make build

# Small runtime image
FROM alpine
RUN apk --update --no-cache add ca-certificates
COPY --from=build-env /go/src/github.com/harrisbaird/dailyteedeals/bin/dailyteedeals /bin/dailyteedeals
CMD ["/bin/dailyteedeals"]
EXPOSE 8080