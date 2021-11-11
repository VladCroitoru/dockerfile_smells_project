FROM golang:onbuild

RUN go build -o /systemd-docker
ADD ./startup.sh /startup.sh

CMD ["/startup.sh"]
