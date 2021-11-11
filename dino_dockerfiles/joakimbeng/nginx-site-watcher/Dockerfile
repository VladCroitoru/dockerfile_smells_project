FROM nginx

ADD run.sh /
ADD watcher.sh /
ADD nginx.conf /etc/nginx/
ADD proxy_params /etc/nginx/

WORKDIR /

RUN chmod +x run.sh watcher.sh

CMD ["./run.sh", "/etc/nginx/sites-enabled"]
