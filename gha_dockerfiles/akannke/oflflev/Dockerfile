FROM golang:1.17.1
WORKDIR /app
COPY go.mod ./
COPY go.sum ./
RUN go mod download
COPY pkg ./pkg
COPY cmd ./cmd
RUN go build -o /ofcev ./cmd
ENTRYPOINT ["/ofcev"]
