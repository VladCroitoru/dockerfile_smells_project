FROM golang:latest AS builder

WORKDIR /src
COPY . .

RUN go build -o /out/my-bin .

FROM scratch AS bin
COPY --from=builder /out/my-bin /
ENTRYPOINT ["/my-bin"]
