FROM clouder/clouder-base
MAINTAINER Yannick Buron yburon@goclouder.net

RUN apt-get -qq update && DEBIAN_FRONTEND=noninteractive apt-get -y -qq install git

RUN git clone http://github.com/odoo/odoo.git /opt/odoo/files/odoo -b 10.0
RUN mkdir /opt/odoo/files/extra

ADD sources/http.patch /tmp/http.patch
RUN patch /opt/odoo/files/odoo/odoo/http.py < /tmp/http.patch
