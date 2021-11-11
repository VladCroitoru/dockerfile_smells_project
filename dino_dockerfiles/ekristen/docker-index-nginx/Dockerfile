FROM dockerfile/nginx
MAINTAINER "Erik Kristensen <erik@erikkristensen.com>"

VOLUME ["/etc/nginx/ssl"]

ADD ssl/ /etc/nginx/ssl/
ADD default /etc/nginx/sites-enabled/default
ADD run.sh /run.sh

CMD ["bash", "/run.sh"]
