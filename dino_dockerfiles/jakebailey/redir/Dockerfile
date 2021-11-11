FROM golang:alpine as builder

RUN apk update && apk add --no-cache git ca-certificates
RUN adduser -D -g '' appuser

WORKDIR /src

COPY ./go.mod ./go.sum ./
RUN go mod download

COPY ./ ./

RUN CGO_ENABLED=0 go build -v -ldflags="-w -s" -o /app

FROM scratch

COPY --from=builder /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=builder /etc/passwd /etc/passwd
COPY --from=builder /app /app

USER appuser
EXPOSE 5000
ENTRYPOINT [ "/app" ]
