FROM nginx:1.10.0

ADD nginx.conf /etc/nginx/nginx.conf
ADD nginx.vh.default.conf /etc/nginx/conf.d/default.conf

ADD ./run.sh /run.sh

EXPOSE 80

ENTRYPOINT ["/run.sh"]
