FROM alpine:latest

RUN apk update && apk add openssh supervisor
RUN /usr/bin/ssh-keygen -A

EXPOSE 3306

CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]

COPY files/ /
