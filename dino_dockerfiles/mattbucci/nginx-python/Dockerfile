FROM nginx:latest
MAINTAINER Matthew Bucci <mtbucci@gmail.com>

RUN \
  DEBIAN_FRONTEND=noninteractive \
  apt-get -q -y update && \
  apt-get -q -y install fcgiwrap wget gnupg lsb-release && \
  apt-get -q -y update && \
  apt-get -q -y install python-subversion subversion && \
  sed -i 's/^\(user .*\)$/user root;/' /etc/nginx/nginx.conf

CMD nginx && spawn-fcgi -s /var/run/fcgiwrap.sock /usr/sbin/fcgiwrap -n