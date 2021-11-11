# Run the build
FROM golang:alpine
ENV WORKDIR /go/src/github.com/tirithen/unit-conversion
COPY . $WORKDIR
WORKDIR $WORKDIR
RUN apk --update add git
RUN go get -t -v ./...
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build

# Create the final docker image
FROM scratch
COPY --from=0 /go/src/github.com/tirithen/unit-conversion/unit-conversion /
COPY --from=0 /go/src/github.com/tirithen/unit-conversion/converter.yml /
EXPOSE 8080
ENTRYPOINT ["/unit-conversion"]
