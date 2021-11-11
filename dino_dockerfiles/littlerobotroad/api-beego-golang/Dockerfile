FROM golang:1.8.1
MAINTAINER LittleRobot daisukeayanami@gmail.com

# Install beego & bee
RUN go get -u github.com/astaxie/beego
RUN go get -u github.com/beego/bee
RUN go get -u github.com/go-sql-driver/mysql

EXPOSE 8080


ADD / /go/src/github.com/LittleRobotRoad/api-beego-golang

ADD run.sh /

RUN chmod +x /run.sh

CMD ["/run.sh"]
