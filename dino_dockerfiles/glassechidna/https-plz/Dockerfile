FROM nginx:alpine
RUN \
  echo 'server {' > /etc/nginx/conf.d/default.conf && \ 
  echo '    listen         80;' >> /etc/nginx/conf.d/default.conf && \
  echo '    return 301 https://$host$request_uri;' >> /etc/nginx/conf.d/default.conf && \
  echo '}' >> /etc/nginx/conf.d/default.conf
