FROM golang:1.16-alpine as build

WORKDIR /app
COPY . .
RUN go mod download
RUN go build -o /docker-lspd

FROM alpine:3.11.3
COPY --from=build /docker-lspd /docker-lspd

EXPOSE 5051

ENTRYPOINT ["/docker-lspd"]