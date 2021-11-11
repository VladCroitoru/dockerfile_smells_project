FROM golang:1.16-alpine
WORKDIR /app
COPY go.mod ./
COPY go.sum ./
COPY pkg ./pkg
COPY cmd ./cmd
COPY app ./app

WORKDIR ./pkg/albumdata
RUN go mod download
WORKDIR ../../cmd
RUN go build
CMD ["./cmd"]
