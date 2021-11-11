# Confd / NGINX
#
# Version 0.0.1

FROM centos:7.1.1503

ENTRYPOINT "/boot.sh"

VOLUME ["/php", "/etc/confd"]

EXPOSE 80 

ADD boot.sh /boot.sh

RUN /bin/localedef -v -c -i en_US -f UTF-8 en_US.UTF-8;\
    yum -y install epel-release; \
    yum -y install nginx; \
    yum clean all;\
    curl -L https://github.com/kelseyhightower/confd/releases/download/v0.10.0/confd-0.10.0-linux-amd64 -o /usr/bin/confd;\
    chmod +x /usr/bin/confd;\
    sed -i '/server_name/d' /etc/nginx/nginx.conf;\
    sed -i '/default_server/d' /etc/nginx/nginx.conf
