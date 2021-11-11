FROM golang:1.16-alpine

WORKDIR /app

COPY go.mod ./
COPY go.sum ./
RUN go mod download

COPY . ./
COPY config.yaml /

RUN go build -o /cookbook

CMD [ "/cookbook" ]