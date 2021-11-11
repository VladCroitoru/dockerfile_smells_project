FROM golang:1.17.2 as builder

WORKDIR /app

COPY go.mod .
COPY go.sum .
RUN go mod download

COPY main.go .
COPY config/ config/
COPY domain/ domain/
COPY handler/ handler/
COPY infrastructure/ infrastructure/
RUN CGO_ENABLED=0 go build -o mflight-api

FROM scratch
COPY --from=builder /app/mflight-api /bin/mflight-api
ENTRYPOINT ["/bin/mflight-api"]
