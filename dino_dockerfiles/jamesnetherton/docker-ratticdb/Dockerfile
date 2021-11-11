FROM debian:wheezy

ADD https://github.com/tildaslash/RatticWeb/archive/v1.2.1.zip /opt/v1.2.1.zip

RUN apt-get update 
RUN apt-get install -y unzip python python-pip \
python-dev gcc libsqlite3-dev \
libcurl4-openssl-dev libldap2-dev \
libsasl2-dev libxml2-dev libxslt-dev apache2 libapache2-mod-wsgi

RUN cd /opt/ && unzip v1.2.1.zip && rm -f v1.2.1.zip

ADD ./requirements-sqlite.txt /opt/RatticWeb-1.2.1/
ADD ./local.cfg /opt/RatticWeb-1.2.1/conf/local.cfg
ADD ./rattic.conf /etc/apache2/conf.d/sites-enabled/rattic
ADD ./start-apache.sh /start-apache.sh

RUN cd /opt/RatticWeb-1.2.1/ && pip install -r requirements-sqlite.txt
RUN cd /opt/RatticWeb-1.2.1/ && ./manage.py syncdb --noinput && ./manage.py migrate --all
RUN cd /opt/RatticWeb-1.2.1/ && mkdir static && ./manage.py collectstatic -c --noinput
RUN cd /opt/RatticWeb-1.2.1/ && ./manage.py demosetup
RUN chmod +x /start-apache.sh && chown www-data /opt/RatticWeb-1.2.1/ && chown www-data:www-data /opt/RatticWeb-1.2.1/rattic.db

EXPOSE 80

CMD ["/start-apache.sh"]
