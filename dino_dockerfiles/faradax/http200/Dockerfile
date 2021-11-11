FROM golang:latest AS build
RUN mkdir -p /app

COPY main.go /app/main.go

WORKDIR /app

RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o ./http200 ./main.go

FROM scratch
COPY --from=build /app/http200 /http200
CMD ["/http200"]