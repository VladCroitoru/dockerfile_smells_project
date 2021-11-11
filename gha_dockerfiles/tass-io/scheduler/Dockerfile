FROM golang:latest as builder
WORKDIR /code
ADD . /code
RUN go env -w GO111MODULE=on && go env -w GOPROXY=https://goproxy.cn,direct && go mod download
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o app .

FROM centos as prod
EXPOSE 50001
WORKDIR /root/
COPY --from=0 /code/app .
RUN chmod +x /root/app
ENTRYPOINT ["/root/app"]
