FROM keenneeth/http-php
MAINTAINER keenneeth@mail.asix

ADD scriptapache.sh /scriptapache.sh
RUN chmod 700 /scriptapache.sh

EXPOSE 80

CMD ["/scriptapache.sh"]
