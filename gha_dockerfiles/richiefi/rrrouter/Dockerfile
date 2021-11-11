FROM golang:1.16.4-buster
WORKDIR /app
COPY . .
RUN go vet ./...
RUN go test -tags=integration ./...
RUN go install github.com/richiefi/rrrouter/cmd/richie-request-router

FROM debian:buster
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates
RUN update-ca-certificates
COPY --from=0 /go/bin/richie-request-router .
ENTRYPOINT ["./richie-request-router"]
CMD ["start"]

# Document that the service listens on port 5000.
EXPOSE 5000
ENV PORT 5000
