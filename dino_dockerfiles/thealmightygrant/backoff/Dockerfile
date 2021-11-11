FROM golang:1.9.2
WORKDIR /go/src/github.com/thealmightygrant/backoff/
COPY ./main.go .
RUN CGO_ENABLED=0 GOOS=linux go build -tags netgo -ldflags '-w' .

FROM centurylink/ca-certs
COPY --from=0 /go/src/github.com/thealmightygrant/backoff/backoff .
ENTRYPOINT ["/backoff"]
