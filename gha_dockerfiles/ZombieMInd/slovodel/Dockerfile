FROM golang as build-stage
WORKDIR /app

COPY go.mod /app
COPY go.sum /app
RUN go mod download

COPY cmd/api/main.go /app
COPY internal/ /app/internal

RUN cd /app && CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app

FROM alpine
COPY --from=build-stage /app/app /
COPY .env /

EXPOSE 8080

CMD ["/app"]