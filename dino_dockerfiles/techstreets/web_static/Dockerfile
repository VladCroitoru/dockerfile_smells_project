FROM nginx:1.10.3
MAINTAINER bradojevic@gmail.com

RUN apt-get update && apt-get install -y \
    gcc gettext net-tools curl wget vim git python-pip \
    --no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV SUPERVISOR_VERSION 3.1.0
ENV APP_ROOT /opt/app

# Define working directory.
RUN mkdir -p ${APP_ROOT}

# config nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN ln -s /opt/app/nginx/web_static.conf /etc/nginx/conf.d/default.conf
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

EXPOSE 80 443 8080 3000

CMD ["/usr/local/bin/supervisord"]
