FROM ansi/mosquitto
MAINTAINER Alexandre Vasconcellos, alexv@cpqd.com.br

USER root
RUN apt-get update \
	&& apt-get install -y python-openssl python-pip uwsgi-plugin-python nginx supervisor \
	&& pip install uwsgi flask requests kafka

RUN  mkdir -p /var/www/app
COPY *.py  /var/www/app/

COPY mosquitto-files/access.acl /usr/local/src/mosquitto-1.4.13/certs/access.acl
COPY mosquitto-files/mosquitto.conf /usr/local/src/mosquitto-1.4.13/mosquitto.conf
COPY initialConf.py /usr/local/src/mosquitto-1.4.13/initialConf.py
COPY certUtils.py /usr/local/src/mosquitto-1.4.13/certUtils.py
COPY entrypoint.sh /usr/local/src/mosquitto-1.4.13/

COPY docker/nginx/flask.conf /etc/nginx/sites-available/
COPY docker/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker/app/uwsgi.ini /var/www/app/uwsgi.ini

RUN mkdir -p /var/log/nginx/app /var/log/uwsgi/app /var/log/supervisor  /var/www/app/icons   && \
	ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf && \
    echo "daemon off;" >> /etc/nginx/nginx.conf && \
    chown -R www-data:www-data /var/www/app && \
	chown -R www-data:www-data /var/log && \
	chown -R mosquitto /usr/local/src/mosquitto-1.4.13/ && \
	chmod +x /usr/local/src/mosquitto-1.4.13/entrypoint.sh  && \
	chmod +x /usr/local/src/mosquitto-1.4.13/initialConf.py && \
	ln /var/www/app/conf.py /usr/local/src/mosquitto-1.4.13/conf.py

EXPOSE 8883
CMD ["/usr/local/src/mosquitto-1.4.13/entrypoint.sh"]
