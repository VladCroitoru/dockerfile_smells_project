FROM golang:1.8

WORKDIR /src
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o app .

FROM scratch
WORKDIR /app
COPY --from=0 /src/app /app/
ENTRYPOINT ["./app"]

