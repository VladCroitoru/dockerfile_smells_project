FROM nginx:1.12.1-alpine

COPY default.conf /etc/nginx/conf.d/default.conf

ADD start.sh /start.sh
RUN chmod 700 /start.sh

ENV TARGET_PROTO http
EXPOSE 80

CMD ["./start.sh"]
