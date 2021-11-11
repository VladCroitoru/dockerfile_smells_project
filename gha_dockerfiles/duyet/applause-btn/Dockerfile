FROM golang:1.14 AS build
WORKDIR /go/src/github.com/duyet/applause-btn
COPY . .
RUN go mod download
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -installsuffix cgo -o app .

FROM alpine:latest
WORKDIR /app
ENV DB_LOCATION="/tmp/badger" \
    HEADER_USER_EMAIL="x-authenticated-user-email" \
    HEADER_USER_ID="x-authenticated-uid"
RUN mkdir ./public
COPY ./public ./public
COPY --from=build /go/src/github.com/duyet/applause-btn/app .
EXPOSE 3000
CMD ["./app"]