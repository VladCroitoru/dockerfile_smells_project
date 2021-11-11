FROM alpine:3.4

RUN apk add --no-cache py-pip mysql-client \
 && pip install awscli

ENV FILENAME       mysql-backup
ENV MYSQL_PORT     3306
ENV MYSQL_USER     root
ENV MYSQL_PASSWORD ''

ADD entry.sh /usr/bin/

ENTRYPOINT ["/usr/bin/entry.sh"]
CMD ["backup"]