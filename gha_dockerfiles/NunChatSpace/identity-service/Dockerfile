FROM golang:1.16
WORKDIR /app
COPY . .

RUN go mod tidy
CMD ["go", "run", ".", "serve"] 