FROM python:2.7
MAINTAINER Philip Berndroth <p.berndroth@philuweb.de>

WORKDIR /opt/netbox

ARG BRANCH="master"
ARG URL="https://github.com/digitalocean/netbox.git"
ARG ENTRY_SCRIPT="https://raw.githubusercontent.com/digitalocean/netbox/master/docker/docker-entrypoint.sh"
ARG CONFIG_SCRIPT="https://raw.githubusercontent.com/digitalocean/netbox/master/netbox/netbox/configuration.docker.py"
ARG GUNICORN_CONF="https://raw.githubusercontent.com/digitalocean/netbox/master/docker/gunicorn_config.py"
ARG NGINX_CONF="https://raw.githubusercontent.com/digitalocean/netbox/master/docker/nginx.conf"

RUN git clone --depth 1 $URL -b $BRANCH .

RUN apt-get update -qq && apt-get install -y libldap2-dev libsasl2-dev libssl-dev graphviz nginx && \
    pip install gunicorn==17.5 && \
    pip install django-auth-ldap && \
    pip install -r requirements.txt

ADD $ENTRY_SCRIPT /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ADD $CONFIG_SCRIPT /opt/netbox/netbox/netbox/configuration.py
ADD $GUNICORN_CONF /opt/netbox/

ADD $NGINX_CONF /etc/nginx/nginx.conf

EXPOSE 80
ENTRYPOINT [ "/docker-entrypoint.sh" ]
