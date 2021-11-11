FROM golang:1.9
WORKDIR /go/src/github.com/jsantiagoh/trivial-server
COPY main.go .
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM scratch
WORKDIR /app
COPY --from=0 /go/src/github.com/jsantiagoh/trivial-server/app .
EXPOSE 8080
CMD ["./app"]  
