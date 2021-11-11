FROM alpine

RUN apk update && apk upgrade
RUN apk add mysql-client

COPY start.sh /usr/bin/start.sh
COPY tasks/ /etc/periodic

RUN chmod +x /usr/bin/start.sh
RUN chmod -R +x /etc/periodic
RUN mkdir -p /backup

WORKDIR /backup

CMD start.sh
