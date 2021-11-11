FROM alpine:latest

WORKDIR /app
VOLUME /app
COPY startup.sh /startup.sh
RUN chmod 755 /startup.sh && chmod +x /startup.sh

RUN apk add --update mysql mysql-client && rm -f /var/cache/apk/*
RUN mkdir /docker-entrypoint-initdb.d
COPY my.cnf /etc/mysql/my.cnf

EXPOSE 3306
CMD ["/startup.sh"]
