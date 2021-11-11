FROM python:2.7.12
MAINTAINER bradojevic@gmail.com

RUN apt-get update && apt-get install -y \
    gcc gettext sqlite3 \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV NGINX_VERSION 1.6.2-5+deb8u4
ENV GUNICORN_VERSION 19.4.1
ENV SUPERVISOR_VERSION 3.1.0
ENV APP_ROOT /opt/app

# Define working directory.
RUN mkdir -p ${APP_ROOT}
# install common tools
RUN apt-get update && apt-get install -y net-tools curl wget vim git
RUN pip install --upgrade pip
# install nginx
RUN apt-get update && apt-get install -y nginx=${NGINX_VERSION}
RUN rm /etc/nginx/sites-enabled/default
RUN ln -s /opt/app/nginx/socket_config /etc/nginx/sites-enabled/default
# install gunicorn
RUN pip install gunicorn==${GUNICORN_VERSION}
# install supervisor
RUN pip install supervisor==${SUPERVISOR_VERSION}
RUN echo_supervisord_conf > /etc/supervisord.conf
RUN mkdir -p /etc/supervisord.d
RUN echo '\
[include]\n\
files = /etc/supervisord.d/*.conf'\
>> /etc/supervisord.conf
RUN ln -s /opt/app/supervisor/supervisor.conf /etc/supervisord.d/supervisor.conf

WORKDIR ${APP_ROOT}
VOLUME ['${APP_ROOT}']

EXPOSE 80 443 5000 5001

CMD ["/usr/local/bin/supervisord"]
