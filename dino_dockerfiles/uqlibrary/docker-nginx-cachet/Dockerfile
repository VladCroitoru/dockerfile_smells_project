FROM uqlibrary/docker-base:9

RUN \
  yum install -y nginx && \
  yum clean all && \
  echo 'fastcgi_param HTTP_PROXY "";' >> /etc/nginx/fastcgi.conf && \
  echo 'fastcgi_buffers 8 8k;' >> /etc/nginx/fastcgi.conf && \
  echo 'fastcgi_buffer_size 8k;' >> /etc/nginx/fastcgi.conf && \
  echo 'fastcgi_busy_buffers_size 16k;' >> /etc/nginx/fastcgi.conf

COPY etc/nginx.conf /etc/nginx/nginx.conf
COPY etc/site.conf /etc/nginx/conf.d/site.conf
COPY etc/h5bp /etc/nginx/h5bp

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
