FROM nginx
EXPOSE 80
EXPOSE 443

COPY nginx.conf /etc/nginx/nginx.conf
COPY run.sh /run.sh
RUN chmod a+x /run.sh && \
    openssl req \
            -new \
            -subj '/CN=*/O=Purple Booth LTD/C=GB' \
            -newkey rsa:2048 -days 1000 -nodes -x509 -keyout /certificate.key -out /certificate.crt

CMD /run.sh
