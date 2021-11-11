FROM debian:jessie
# Initially was based on work of Alessandro Viganò
MAINTAINER CoeusITE <coeusite@gmail.com>

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && apt-get upgrade -y && \
    apt-get install -y ca-certificates nginx net-tools wget curl supervisor apt-utils && \
    apt-get install -y python2.7 python-setuptools python-imaging python-ldap python-mysqldb python-memcache python-urllib3 && \
    apt-get clean all && \
    sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf

RUN mkdir /opt/seafile/logs -p && \
    cd /opt/seafile/ && \
    wget https://bintray.com/artifact/download/seafile-org/seafile/seafile-server_6.0.7_x86-64.tar.gz && \
    tar xzf seafile-server_* && \
    mkdir installed && \
    mv seafile-server_* installed

# Env
ENV SERVER_NAME=SeaDrive SERVER_ADDR=127.0.0.1 ADMIN_EMAIL=admin@example.com ADMIN_PASSWORD=changeme!

# Nginx
ADD seafile-nginx.conf /etc/nginx/sites-available/seafile
# Supervisor
ADD seafile-supervisord.conf /etc/supervisor/conf.d/seafile-supervisord.conf
# bootstrap
ADD bootstrap-data.sh /usr/local/sbin/bootstrap

# Expose needed ports.
EXPOSE 8080

# Volumes
VOLUME ["/etc/nginx", "/opt/seafile", "/etc/supervisor/conf.d"]

# CMD
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

# docker build -t docker-seafile:jessie .
