FROM nginx:latest

ADD https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-0.11.0-linux-amd64 /bin/confd
RUN chmod +x /bin/confd
ADD confd /etc/confd

ADD start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]