FROM nginx:alpine

MAINTAINER Marcel Boogert <marcel@mtdb.nl>

ADD index.sh /tmp/index.sh

RUN chmod +x /tmp/index.sh

RUN /tmp/index.sh

EXPOSE 80
