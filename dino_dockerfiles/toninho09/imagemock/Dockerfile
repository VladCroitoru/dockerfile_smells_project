FROM golang:1.9.2 as builder
WORKDIR /app
RUN go get -u github.com/fogleman/gg
RUN go get -u github.com/gin-gonic/gin
RUN go get -u github.com/lucasb-eyer/go-colorful
COPY .  .
RUN CGO_ENABLED=0 GOOS=linux go build -o imagemock .

FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /app/imagemock .
COPY --from=builder /app/Roboto-Medium.ttf .
EXPOSE 8080
CMD ["./imagemock"]