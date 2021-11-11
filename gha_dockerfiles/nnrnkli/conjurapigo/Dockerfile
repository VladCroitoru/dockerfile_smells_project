FROM golang
RUN mkdir /app
COPY main.go /app/main.go
WORKDIR /app
RUN go build -o main .
CMD ["/app/main"]