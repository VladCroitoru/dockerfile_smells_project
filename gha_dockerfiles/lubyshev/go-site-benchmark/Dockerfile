FROM golang as builder
WORKDIR /build
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -a -o app ./main.go

FROM alpine
MAINTAINER Nick Lubyshev <lubyshev@gmail.com>

ENV APP_SERVER_PORT=8090 \
 APP_CACHE_BACKGROUND_FREQUENCY=30 \
 APP_CACHE_DEBUG=no \
 APP_CACHE_TTL=300 \
 APP_OVERLOAD_QUEUE_WORKERS=8 \
 APP_OVERLOAD_INIT_CONNECTIONS=32 \
 APP_OVERLOAD_MAX_LIMIT=1024 \
 APP_OVERLOAD_MAX_CONNECTIONS=4096

EXPOSE $APP_SERVER_PORT

RUN mkdir /runtime;mkdir /runtime/data
WORKDIR /runtime
COPY --from=builder /build/app /runtime/app

ENTRYPOINT [ "/runtime/app" ]
