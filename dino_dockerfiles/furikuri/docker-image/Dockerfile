FROM golang:1.7.0-alpine

RUN mkdir /app 
ADD . /app/
WORKDIR /app 

RUN go build -o main .

ENTRYPOINT ["/app/main"]