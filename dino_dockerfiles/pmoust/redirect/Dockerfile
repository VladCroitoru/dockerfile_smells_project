FROM dockerfile/ubuntu

MAINTAINER Panagiotis Moustafellos <pmoust@gmail.com>

RUN \
  add-apt-repository -y ppa:nginx/stable && \
  apt-get update && \
  apt-get install -y nginx && \
  chown -R www-data:www-data /var/lib/nginx

ADD nginx.conf /etc/nginx.conf

ADD redirect.sh /redirect.sh
RUN chmod +x /redirect.sh

ENTRYPOINT ["/bin/bash", "/redirect.sh"]
EXPOSE 80
