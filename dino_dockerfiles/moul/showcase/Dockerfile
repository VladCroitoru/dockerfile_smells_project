FROM golang:1.14
COPY . /go/src/github.com/moul/showcase
WORKDIR /go/src/github.com/moul/showcase
RUN go install -v ./cmd/moul-showcase
CMD ["moul-showcase", "server"]
EXPOSE 8080
