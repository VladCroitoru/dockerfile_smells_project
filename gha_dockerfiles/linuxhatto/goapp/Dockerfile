FROM golang:1.17
WORKDIR /app
COPY main.go .
RUN CGO_ENABLE=0 go build -o server main.go
EXPOSE 8080
CMD [ "./server" ]
