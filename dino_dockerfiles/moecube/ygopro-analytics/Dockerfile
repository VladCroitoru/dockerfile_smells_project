FROM golang

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

WORKDIR /usr/src/app
COPY . /usr/src/app
RUN go get -d -v ./...
RUN go build -v main.go

ENTRYPOINT /usr/src/app/main