FROM golang:1.9
WORKDIR /go/src/http
COPY . .
RUN go get ./
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM scratch
COPY --from=0 /go/src/http/app/app
COPY --from=0 /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
CMD ["/app"]
