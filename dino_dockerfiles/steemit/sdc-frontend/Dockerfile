FROM phusion/baseimage:0.9.19

RUN \
    apt-get update && \
    apt-get install -y \
        nginx-full \
        gettext \
    && \
    apt-get clean

ADD startservices.sh /usr/bin/startservices.sh

RUN chmod +x /usr/bin/startservices.sh

ADD site* /etc/nginx/

ADD nginx.conf.template /etc/nginx/nginx.conf.template

EXPOSE 8081

CMD /usr/bin/startservices.sh
