FROM ubuntu:14.04

MAINTAINER Gadi Srebnik <gadi@rounds.com>

RUN apt-get update && apt-get install -y --force-yes nginx
ADD default /etc/nginx/sites-enabled/default

CMD nginx -g 'daemon off;'
EXPOSE 80
