FROM golang:1.9.2-alpine3.6
ARG VERSION
WORKDIR /go/src/github.com/nordicdyno/centrifugo_exporter
COPY . .
RUN echo "RUN go build..."
RUN go build -ldflags "-X 'main.VERSION=${VERSION}'" -o centrifugo_exporter .

FROM alpine:3.6
RUN echo "build alpine based image..."
RUN apk --no-cache add ca-certificates
WORKDIR /bin/
COPY --from=0 /go/src/github.com/nordicdyno/centrifugo_exporter/centrifugo_exporter .
CMD ["centrifugo_exporter"]
ENTRYPOINT ["/bin/centrifugo_exporter"]
