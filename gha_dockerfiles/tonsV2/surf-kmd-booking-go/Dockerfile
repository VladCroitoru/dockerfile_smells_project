FROM golang:1.16-alpine AS build
WORKDIR /src
RUN go get github.com/cespare/reflex
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN go build -o /app/surf-kmd-booking -ldflags "-s -w" ./cmd/app

FROM alpine:3.13
RUN apk --no-cache -U upgrade
WORKDIR /app
COPY --from=build /app/surf-kmd-booking .
COPY ./templates ./templates/
USER guest
CMD ["/app/surf-kmd-booking"]
