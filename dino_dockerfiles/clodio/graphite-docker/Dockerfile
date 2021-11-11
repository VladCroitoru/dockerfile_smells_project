FROM	ubuntu:14.04

MAINTAINER claude.seguret@gmail.com
 
RUN	apt-get -y update

# Install required packages
RUN	apt-get -y install python-ldap python-cairo python-django python-twisted python-django-tagging python-simplejson python-memcache python-pysqlite2 python-support python-pip gunicorn supervisor nginx-light
RUN	pip install whisper
RUN	pip install --install-option="--prefix=/var/lib/graphite" --install-option="--install-lib=/var/lib/graphite/lib" carbon
RUN	pip install --install-option="--prefix=/var/lib/graphite" --install-option="--install-lib=/var/lib/graphite/webapp" graphite-web

# Add supervisord
RUN	apt-get -y install supervisor
ADD	./supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Add graphite config
ADD	./nginx.conf /etc/nginx/nginx.conf
ADD	./initial_data.json /var/lib/graphite/webapp/graphite/initial_data.json
ADD	./local_settings.py /var/lib/graphite/webapp/graphite/local_settings.py
ADD	./carbon.conf /var/lib/graphite/conf/carbon.conf
ADD	./storage-schemas.conf /var/lib/graphite/conf/storage-schemas.conf
ADD	./storage-aggregation.conf /var/lib/graphite/conf/storage-aggregation.conf
RUN	mkdir -p /var/lib/graphite/storage/whisper
RUN	mkdir -p /var/log/graphite
RUN	chown -R www-data /var/log/graphite
RUN ln -s /var/lib/graphite /opt/graphite 
RUN	touch /var/lib/graphite/storage/graphite.db /var/lib/graphite/storage/index
RUN	chown -R www-data /var/lib/graphite/storage
RUN	chmod 0775 /var/lib/graphite/storage /var/lib/graphite/storage/whisper
RUN	chmod 0664 /var/lib/graphite/storage/graphite.db
RUN	cd /var/lib/graphite/webapp/graphite && python manage.py syncdb --noinput

# Install collectd
RUN	apt-get -y install collectd collectd-utils
ADD	./collectd.conf /etc/collectd/collectd.conf

# Nginx
EXPOSE	:80
# Carbon line receiver port
EXPOSE	:2003
# Carbon pickle receiver port
EXPOSE	:2004
# Carbon cache query port
EXPOSE	:7002

VOLUME ["/var/lib/graphite/storage", "/var/log"]

CMD	["/usr/bin/supervisord"]
