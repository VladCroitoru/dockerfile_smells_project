FROM golang AS build-env
RUN CGO_ENABLED=0 go get github.com/okzk/metaflake

FROM alpine
RUN apk add --no-cache ca-certificates
COPY --from=build-env /go/bin/metaflake /usr/local/bin/
EXPOSE 8000
CMD ["metaflake"]
