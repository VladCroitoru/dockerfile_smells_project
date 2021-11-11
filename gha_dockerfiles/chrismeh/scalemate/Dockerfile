FROM golang:alpine

ENV ADDR ":8080"

RUN apk add --no-cache git
WORKDIR /app
ADD . ./

RUN go build -o web ./cmd/web

CMD ["sh", "-c", "./web -addr=${ADDR}"]