FROM          ubuntu:12.04
MAINTAINER    Drew Carey Buglione <drew@etymonline.com>

RUN           DEBIAN_FRONTEND=noninteractive apt-get install -y wget
RUN           wget http://nginx.org/packages/keys/nginx_signing.key -O- | apt-key add -
RUN           echo "deb http://nginx.org/packages/ubuntu/ precise nginx" >> /etc/apt/sources.list && apt-get update
RUN           DEBIAN_FRONTEND=noninteractive apt-get install -y nginx
RUN           echo "daemon off;" >> /etc/nginx/nginx.conf
RUN           rm /etc/nginx/conf.d/default.conf
ADD           etymonline.conf /etc/nginx/conf.d/etymonline.conf

EXPOSE        80
ADD           etymonline-nginx.sh /root/etymonline-nginx.sh
CMD           ["/root/etymonline-nginx.sh"]
