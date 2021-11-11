FROM centos:centos7

RUN \
  yum clean all && \
  yum install -y git && \
  mkdir /data && \
  cd /data && \
  git clone https://github.com/projectcalico/canal && \
  mv canal/* . && \
  rm -rf canal

FROM nginx:alpine
COPY --from=0 /data /data
RUN echo "server {autoindex off; server_name localhost; location ~ ^/$ {return 200;} location ~ ^.*/$ {return 404;} location / { root /data; default_type application/octet-stream; add_header Content-Disposition 'attachment'; types {}}}" > /etc/nginx/conf.d/default.conf
