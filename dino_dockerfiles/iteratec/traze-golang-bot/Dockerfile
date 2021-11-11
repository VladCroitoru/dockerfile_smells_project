FROM golang:1-alpine as builder
RUN addgroup -S traze && adduser -S -G traze traze

ARG APP="$GOPATH/traze-golang-bot"
ADD . $APP

RUN apk add --no-cache git
RUN go get github.com/op/go-logging
RUN go get github.com/eclipse/paho.mqtt.golang

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o $APP/main $APP/main.go

# ------------------- Cut Here ------------------ #

FROM scratch
COPY --from=builder /go/traze-golang-bot/main /
COPY --from=builder /etc/passwd /etc/passwd

USER traze
ENTRYPOINT ["/main"]