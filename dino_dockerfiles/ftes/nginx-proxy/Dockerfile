FROM jwilder/nginx-proxy

#RUN mkdir /etc/nginx/conf.d
RUN echo 'proxy_cache_path /tmp/nginx-cache levels=1:2 keys_zone=nginx-cache:10m max_size=4g inactive=60m use_temp_path=off;' \
  > /etc/nginx/conf.d/cache.conf

RUN mkdir /etc/nginx/vhost.d
RUN echo 'proxy_cache nginx-cache;\n\
proxy_cache_bypass $http_cache_control;\n\
proxy_cache_revalidate on;' \
  > /etc/nginx/vhost.d/default

RUN echo 'add_header X-Proxy-Cache $upstream_cache_status;' \
  > /etc/nginx/vhost.d/default_location

# remove buffering=off (prevents caching)
RUN sed -i '/proxy_buffering off;/d' nginx.tmpl

VOLUME /etc/nginx/conf.d
VOLUME /etc/nginx/vhost.d
