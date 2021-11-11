FROM instrumentisto/glide:0.13.0 as builder
WORKDIR /go/src/github.com/scalify/spring_exporter/

COPY glide.yaml glide.lock ./
RUN glide install --strip-vendor

COPY . ./
RUN CGO_ENABLED=0 go build -a -ldflags '-s' -installsuffix cgo -o bin/spring_exporter .


FROM alpine:latest
RUN apk --no-cache add ca-certificates
WORKDIR /root/
COPY --from=builder /go/src/github.com/scalify/spring_exporter/bin/spring_exporter .
RUN chmod +x spring_exporter
ENTRYPOINT ["./spring_exporter"]
