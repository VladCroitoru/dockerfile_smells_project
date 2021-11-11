FROM jwilder/nginx-proxy
RUN { \
      echo 'server_tokens off;'; \
      echo 'client_max_body_size 100m;'; \
      echo 'large_client_header_buffers 4 2048k;'; \
    } > /etc/nginx/conf.d/my_proxy.conf
