FROM nginx
MAINTAINER Vladimir Iakovlev <nvbn.rm@gmail.com>
RUN rm /etc/nginx/conf.d/*
COPY web.conf /etc/nginx/conf.d/

RUN mkdir -p  /var/lib/nginx/cache
RUN chown -R nginx /var/lib/nginx/cache
RUN chmod 700 /var/lib/nginx/cache
