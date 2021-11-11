FROM golang:1.14.4-alpine3.12
ADD . /root/
WORKDIR /root
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -v -x ec2-testing.go && chmod +x ec2-testing

FROM alpine:3.12
WORKDIR /root
COPY --from=0 /root/ec2-testing .
RUN echo "build date: $(date -u)" > date.txt
EXPOSE 8080
CMD ["./ec2-testing"]
