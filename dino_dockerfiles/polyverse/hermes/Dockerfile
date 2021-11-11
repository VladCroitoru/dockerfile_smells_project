FROM golang
WORKDIR /go/src/github.com/polyverse/hermes
COPY . .
WORKDIR /go/src/github.com/polyverse/hermes/standalone
RUN go get -v ./...
RUN GOOS=linux CGO_ENABLED=0 go build

FROM scratch
EXPOSE 9091
COPY --from=0 /go/src/github.com/polyverse/hermes/standalone/standalone /
ENTRYPOINT ["/standalone"]
