FROM golang:1.17-alpine AS build

WORKDIR /src/
COPY . /src/
RUN apk update && apk add --no-cache git ca-certificates tzdata && update-ca-certificates
RUN CGO_ENABLED=0 go build -o /bin/app cmd/app/main.go

FROM scratch
COPY --from=build /bin/app /bin/app
COPY --from=build /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/
COPY --from=build /usr/share/zoneinfo /usr/share/zoneinfo
ENV TZ=Europe/Moscow
WORKDIR /bin/
ENTRYPOINT ["/bin/app"]