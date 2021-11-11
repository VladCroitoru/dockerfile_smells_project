# Build stage
FROM golang:alpine as build

ENV GO111MODULE=on \
  CGO_ENABLED=0 \
  GOOS=linux \
  GOARCH=amd64

WORKDIR /build

COPY go.mod .
COPY . .

RUN go mod download

RUN go build -o main ./cmd/

# Run stage
FROM gcr.io/distroless/cc-debian10

COPY --from=build /build/main .

EXPOSE 8080

CMD ["/main"]