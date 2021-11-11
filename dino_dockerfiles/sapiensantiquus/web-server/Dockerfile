FROM golang:alpine3.7
ADD webserver.go /var/tmp/webserver.go
RUN cd /var/tmp && go build webserver.go && cp /var/tmp/webserver /usr/local/bin/webserver && chmod u+x /usr/local/bin/webserver && mkdir /var/www
EXPOSE 3000
CMD /usr/local/bin/webserver

