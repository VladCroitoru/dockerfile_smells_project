# -----------------------------------------------------------------
# The first stage container, for builiding the application
# -----------------------------------------------------------------
FROM golang:1.17 as builder

ENV GO111MODULE=on \
    CGO_ENABLED=0 \
    GOOS=linux \
    GOARCH=amd64

WORKDIR /build

COPY . .

RUN make build 

# -----------------------------------------------------------------
# The second stage container, for running the application
# -----------------------------------------------------------------
FROM alpine:3.14
COPY --from=builder /build/bin/sharechat /app/sharechat
COPY --from=builder /build/migrations /app/migrations
WORKDIR /app

ENTRYPOINT [ "/app/sharechat" ]