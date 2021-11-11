#Build Builder aplication
FROM golang
WORKDIR /var/app
COPY . .
RUN go build main.go
CMD ["/var/app/main"]