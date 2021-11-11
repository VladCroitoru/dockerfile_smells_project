FROM nginx:alpine

ADD nginx.default.conf /etc/nginx/conf.d/default.conf

COPY bootstrap.sh /bootstrap.sh

ENTRYPOINT ["sh","/bootstrap.sh"]
