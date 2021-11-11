FROM golang:1.16-alpine

RUN mkdir -p /app/test

COPY . /app/test

WORKDIR /app/test

RUN go mod vendor
RUN go build .

ENTRYPOINT ["./test"]