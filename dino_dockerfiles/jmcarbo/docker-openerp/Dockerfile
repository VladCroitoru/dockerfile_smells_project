# openerp app
#
# Usage: docker run dpaw/openerp [provisionAndRun|run|provision]
#
# Description: based on
#              http://www.theopensourcerer.com/2012/12/how-to-install-openerp-7-0-on-ubuntu-12-04-lts/
#
# Sets: 
#
# Exposes: 8080/openerp
#

FROM ubuntu:14.04
MAINTAINER Joan Marc Carbo Arnau <jmcarbo@gmail.com>

RUN apt-get update
RUN apt-get install -q -y language-pack-en
RUN update-locale LANG=en_US.UTF-8

RUN apt-get install -q -y vim

# project settings
ENV project_name openerp
ENV project_root /home/openerp/
ENV project_url http://nightly.openerp.com/7.0/nightly/src/openerp-7.0-latest.tar.gz

RUN adduser --system --home=$project_root --group openerp && \
    apt-get -y install python-dateutil python-docutils python-feedparser \
        python-gdata python-jinja2 python-libxslt1 \
        python-mako python-mock python-openid python-psutil \
        python-pybabel python-pychart python-pydot python-pyparsing \
        python-simplejson python-tz python-unittest2 \
        python-vatnumber python-vobject python-webdav python-werkzeug \
        python-xlwt python-yaml python-zsi python-reportlab python-psycopg2 \
        postgresql-client python-cups python-django-auth-ldap git

RUN apt-get -y install wget sudo bzip2

RUN    wget https://wkhtmltopdf.googlecode.com/files/wkhtmltoimage-0.11.0_rc1-static-amd64.tar.bz2 && \
    wget https://wkhtmltopdf.googlecode.com/files/wkhtmltopdf-0.11.0_rc1-static-amd64.tar.bz2 && \
    bzip2 -d wkhtmltoimage-0.11.0_rc1-static-amd64.tar.bz2 && \
    tar xvf wkhtmltoimage-0.11.0_rc1-static-amd64.tar && \
    bzip2 -d wkhtmltopdf-0.11.0_rc1-static-amd64.tar.bz2 && \
    tar xvf wkhtmltopdf-0.11.0_rc1-static-amd64.tar && \
    install wkhtmltopdf-amd64 /usr/bin/wkhtmltopdf && \
    install wkhtmltoimage-amd64 /usr/bin/wkhtmltoimage 

#RUN useradd openerp
RUN adduser openerp sudo
RUN echo openerp:vagrant | chpasswd
RUN cd / && \
    git clone https://github.com/jmcarbo/openerp7.git && \
    chown -R openerp: openerp7 && \
    ln -s openerp7/ openerp-server

ADD startup.sh /startup.sh

CMD ["startup.sh"]
EXPOSE 8069
USER openerp
