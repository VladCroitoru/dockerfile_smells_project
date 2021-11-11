FROM pfgray/casa:latest

#Install couchdb:
RUN apt-get update
RUN apt-get install -y couchdb

RUN mkdir /var/run/couchdb

ADD ./run.sh /app/

CMD ["/bin/sh", "-e", "/app/run.sh"]

