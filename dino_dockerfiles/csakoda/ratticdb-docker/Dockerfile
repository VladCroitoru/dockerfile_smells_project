FROM ubuntu:14.04
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"

ENV RATTIC_VERSION master

RUN apt-get update && apt-get install -y build-essential wget
RUN apt-get install -y python2.7 python2.7-dev python-pip
RUN apt-get install -y libsasl2-dev libxml2-dev libxslt-dev libpq-dev libldap2-dev
RUN groupadd rattic && useradd --create-home --home-dir /home/rattic -g rattic rattic

RUN apt-get install -y supervisor nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

ADD nginx-site.conf     /etc/nginx/sites-enabled/default
ADD supervisord.conf    /etc/supervisor/conf.d/

RUN wget   https://github.com/csakoda/RatticWeb/archive/master.tar.gz
RUN tar -xzf /$RATTIC_VERSION.tar.gz -C /srv/
RUN rm /$RATTIC_VERSION.tar.gz
RUN ln -s /srv/RatticWeb-$RATTIC_VERSION /srv/RatticWeb

WORKDIR /srv/RatticWeb

RUN pip install -r requirements-pgsql.txt
RUN pip install jinja2
RUN pip install uwsgi

ADD uwsgi.ini           /srv/RatticWeb/
ADD generate_config.py  /srv/RatticWeb/
ADD config.jinja        /srv/RatticWeb/
ADD start.sh            /srv/RatticWeb/

CMD ["/srv/RatticWeb/start.sh"]

EXPOSE 80
