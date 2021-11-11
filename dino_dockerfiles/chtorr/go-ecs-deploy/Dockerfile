FROM golang:1.9.3 as builder
WORKDIR /go/src/github.com/chtorr/go-ecs-deploy/
COPY . ./
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o go-ecs-migrate src/main.go

FROM scratch  
WORKDIR /root/
COPY --from=builder /go/src/github.com/chtorr/go-ecs-deploy/go-ecs-migrate .
CMD ["./go-ecs-migrate"]  