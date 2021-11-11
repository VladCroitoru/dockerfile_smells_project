FROM nginx

ENV EXPORTED_PORT 16379

ADD nginx.conf /etc/nginx/nginx.conf
ADD run.sh /usr/local/bin/run.sh

EXPOSE ${EXPORTED_PORT}

CMD ["/usr/local/bin/run.sh"]
