FROM golang:1.17.1-alpine3.14 as builder

WORKDIR /build
COPY go.mod go.sum ./

RUN go mod download

ADD . ./

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -ldflags '-extldflags "-static"' -o pomegranate ./cmd/pomegranate

FROM scratch

WORKDIR /app
COPY --from=builder /build/pomegranate /app/

CMD ["./pomegranate"]