FROM ubuntu:14.04
MAINTAINER Luca Mattivi <luca@smartdomotik.com>

RUN apt-get update
RUN apt-get install -y nginx python python-dev python-pip

RUN pip install Jinja2

RUN rm /etc/nginx/sites-enabled/default
ADD html/ /usr/share/nginx/html/
ADD sites-enabled/ /etc/nginx/sites-enabled/
ADD ssl/ /etc/nginx/ssl/
ADD nginx.conf /etc/nginx/

ADD scripts/ /scripts/

VOLUME ["/etc/nginx/ssl/", "/scripts/"]

EXPOSE 80 443

WORKDIR /scripts/
CMD ["python", "startup.py"]
