FROM nginx

MAINTAINER Nic Fellows

ADD run.sh /run.sh
ADD conf/nginx.conf /etc/nginx/nginx.conf
ADD conf/caching-proxy.conf /etc/nginx/conf.d/caching-proxy.conf
ADD conf/resizer.conf /etc/nginx/conf.d/resizer.conf

ENV ASSET_LOCATION changeme

EXPOSE 80

CMD ["/bin/bash", "/run.sh"]
