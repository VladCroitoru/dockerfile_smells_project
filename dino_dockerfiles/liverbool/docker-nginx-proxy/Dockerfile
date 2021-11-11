FROM jwilder/nginx-proxy
MAINTAINER Liverbool nukboon@gmail.com

RUN echo 'Asia/Bangkok' | tee /etc/timezone

RUN { \
      echo 'server_tokens off;'; \
      echo 'client_max_body_size 100m;'; \
    } > /etc/nginx/conf.d/custom_proxy.conf

# RUN
# docker run -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock liverbool/nginx-proxy
