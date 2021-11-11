FROM golang:alpine AS builder
ADD godig.go /app/godig.go
WORKDIR /app
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o godig godig.go
 
FROM scratch
WORKDIR /app
COPY --from=builder /app .
ENTRYPOINT ["./godig"]
