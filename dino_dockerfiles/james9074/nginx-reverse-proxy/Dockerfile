FROM nginx
MAINTAINER James Thomas <james9074@gmail.com>

# Script to rewrite our nginx conf with a desired NGINX_PORT (listening port) and NGINX_HOST (target)
ADD run_nginx.sh /app/

# The pre-written conf file to make this faster
ADD default.conf.template /etc/nginx/conf.d/default.conf.template

# No reason for /app/ specifically, just a safe place to stash the run script
WORKDIR /app/
RUN chmod +x run_nginx.sh

CMD ["./run_nginx.sh"]
