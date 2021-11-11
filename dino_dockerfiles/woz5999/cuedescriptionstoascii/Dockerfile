FROM golang:1.12 as build
WORKDIR $GOPATH/src/github.com/woz5999/CueDescriptionsToASCII
COPY ./ ./
ARG VERSION
RUN mkdir -p /static \
  && cp -r "$GOPATH/src/github.com/woz5999/CueDescriptionsToASCII/static/files" /static/files
RUN GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o /cuedescriptionstoascii

FROM alpine:3.6
WORKDIR /app
COPY --from=build /cuedescriptionstoascii /bin
COPY --from=build /static/files /app/static/files/
ENTRYPOINT ["cuedescriptionstoascii"]
