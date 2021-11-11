FROM uqlibrary/docker-nginx:15

RUN sed -i "s/client_body_timeout 60;/client_body_timeout 180;\nclient_max_body_size 800m;\n/" /etc/nginx/nginx.conf && \
  sed -i "s/keepalive_timeout 10 10;/keepalive_timeout 180 180;\n/" /etc/nginx/nginx.conf && \
  sed -i "s/send_timeout 60;/send_timeout 180;\n/" /etc/nginx/nginx.conf && \
  sed -i "s/fastcgi_busy_buffers_size 32k;/fastcgi_busy_buffers_size 128k;\n/" /etc/nginx/fastcgi.conf && \
  sed -i "s/fastcgi_buffers 8 16k;/fastcgi_buffers 8 64k;\n/" /etc/nginx/fastcgi.conf && \
  sed -i "s/fastcgi_buffer_size 16k;/fastcgi_buffer_size 128k;\n/" /etc/nginx/fastcgi.conf