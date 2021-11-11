FROM golang:1.16-alpine

WORKDIR /app

COPY go.mod ./
COPY go.sum ./

RUN go mod download
COPY *.go ./
RUN go build -o /resizer_bot

EXPOSE 8080

CMD [ "/resizer_bot" ]
