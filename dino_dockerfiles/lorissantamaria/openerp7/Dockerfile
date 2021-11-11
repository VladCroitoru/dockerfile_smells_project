FROM centos
MAINTAINER Loris Santamaria "loris@lgs.com.ve"

RUN rpm -ivh http://dl.fedoraproject.org/pub/epel/6/i386/epel-release-6-8.noarch.rpm
RUN rpm -ivh http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-centos93-9.3-1.noarch.rpm
RUN yum -y install libxslt-python mx poppler-utils \
	postgresql93 postgresql93-libs postgresql93-server \ 
	pychart pydot python-babel python-dateutil python-devel python-docutils \
	python-feedparser python-gdata python-imaging python-jinja2 python-ldap python-lxml \
	python-mako python-matplotlib python-mock python-openid python-psutil \
	python-psycopg2 python-reportlab python-setuptools python-simplejson \
	python-unittest2 python-vatnumber python-vobject python-werkzeug \
	pytz pywebdav PyXML PyYAML

ADD postgresql-9.3  /etc/sysconfig/pgsql/postgresql-9.3

RUN rpm -ivh http://nightly.openerp.com/7.0/nightly/rpm/openerp-7.0_20140430_231250-1.noarch.rpm
RUN rm -rf /usr/local/lib/python2.7/dist-packages/openerp/addons
RUN mv /usr/local/openerp/addons /usr/local/lib/python2.7/dist-packages/openerp
RUN cp /usr/local/openerp/*.py /usr/local/openerp/*.rng /usr/local/lib/python2.7/dist-packages/openerp &>/dev/null
RUN ln -s /var/lib/openerp/filestore /usr/local/lib/python2.7/dist-packages/openerp/filestore
RUN /usr/sbin/adduser -d /var/lib/openerp -r openerp
RUN mkdir /var/run/openerp && chown openerp:openerp /var/run/openerp
ADD openerp-server.conf /etc/openerp-server.conf-default
ADD openerp.init /openerp.init
RUN chmod 755 /openerp.init
RUN rm -f /dev/ttyUB0 /dev/ttyUB1

EXPOSE 8069

VOLUME  ["/var/lib/openerp"]

CMD ["/bin/bash", "-c", "/openerp.init"]
