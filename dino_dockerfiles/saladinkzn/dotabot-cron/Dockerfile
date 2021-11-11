FROM golang:1.16.4 as build
WORKDIR /go/src/dotabot-cron

COPY go.mod .
COPY go.sum .
COPY vendor vendor

COPY dota dota 
COPY matches matches
COPY repository repository
COPY telegram telegram
COPY tests tests
COPY context.go .
COPY main.go .

RUN CGO_ENABLED=0 GOOS=linux go build -a --installsuffix cgo -o dotabot-cron .

FROM alpine:latest
WORKDIR /root 

RUN apk --update --no-cache add ca-certificates

COPY --from=build /go/src/dotabot-cron/dotabot-cron .

COPY docker-entrypoint.sh .

CMD ["./docker-entrypoint.sh"]