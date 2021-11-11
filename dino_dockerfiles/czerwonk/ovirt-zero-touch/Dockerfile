FROM golang as builder
RUN go get -d -v github.com/czerwonk/ovirt-zero-touch
WORKDIR /go/src/github.com/czerwonk/ovirt-zero-touch
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM alpine:latest
ENV API_INSECURE false
ENV DEBUG false
RUN apk --no-cache add ca-certificates
WORKDIR /app
COPY --from=builder /go/src/github.com/czerwonk/ovirt-zero-touch/app ovirt-zero-touch
CMD ./ovirt-zero-touch -debug=$DEBUG -insecure=$API_INSECURE -api-url=$API_URL -username=$API_USER -password=$API_PASS
EXPOSE 11337
