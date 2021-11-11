FROM ennetech/supervisord-php-nginx:latest

RUN curl -L -o /tmp/invoiceplane.zip https://invoiceplane.com/download/v1.5.8

RUN cd /tmp && unzip invoiceplane.zip && rm /tmp/invoiceplane.zip

RUN mkdir -p /webroot

RUN mv /tmp/ip /webroot/public

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
