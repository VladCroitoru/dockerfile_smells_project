FROM golang:1.16
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN go get .
RUN go build -o main .
CMD ["/app/main"]