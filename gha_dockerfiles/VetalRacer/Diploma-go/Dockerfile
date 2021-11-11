#builder
FROM golang:alpine AS builder
WORKDIR /app
COPY go.mod /app
RUN go mod download
COPY . /app
RUN go build -o main ./cmd/app/nhl/main.go

#runner
FROM alpine
WORKDIR /app
COPY migrations /app/migrations/
COPY templates /app/templates/
COPY raw/Diploma-go.pdf /app/raw/Diploma-go.pdf
COPY --from=builder /app/main /app/
#ENV DB_HOST=""
#ENV DB_LOGIN=""
#ENV DB_PASS=""
#ENV DB_HOST=diploma-psqlserver.postgres.database.azure.com

EXPOSE 80


CMD ["/app/main"]
