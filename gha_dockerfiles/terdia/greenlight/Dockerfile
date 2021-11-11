FROM golang:1.17-alpine as builder
    
WORKDIR /go/src/greenlight

COPY go.mod go.sum ./
RUN go mod download
RUN go get gotest.tools/gotestsum

COPY . .

RUN CGO_ENABLED=0 GOOS=linux go build -ldflags='-s' -o /go/bin/api -x /go/src/greenlight/cmd/api

EXPOSE 4000

COPY entrypoint.sh ./entrypoint.sh

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]