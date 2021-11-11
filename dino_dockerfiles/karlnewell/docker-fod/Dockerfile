FROM debian:wheezy

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
 apache2 \
 beanstalkd \
 exim4-daemon-light \
 gcc \
 git \
 gunicorn \
 libapache2-mod-proxy-html \
 libapache2-mod-shib2 \
 libevent-dev \
 libmysqlclient-dev \
 libxml2-dev \
 libxslt-dev \
 libxslt1-dev \
 memcached \
 mysql-client \
 mysql-server \
 python \
 python-dev \
 python-django \
 python-django-celery \
 python-django-registration \
 python-django-tinymce \
 python-gevent \
 python-ipaddr \
 python-lxml \
 python-memcache \
 python-mysqldb \
 python-paramiko \
 python-pip \
 python-yaml \
 tinymce \
 vim \
 && rm -rf /var/lib/apt/lists/*

RUN pip install ncclient djangorestframework==2.4.8 South
RUN git clone https://github.com/karlnewell/nxpy.git && \
    cd nxpy && \
    python setup.py install
RUN cd /srv && \
    git clone https://github.com/grnet/flowspy.git && \
    cd flowspy/flowspy && \
    cp urls.py.dist urls.py
RUN cd /srv && \
    git clone https://github.com/grnet/flowspy-graphs.git && \
    cd flowspy-graphs && \
    python setup.py install
RUN sed -i 's/#START/START/' /etc/default/beanstalkd
RUN mkdir /var/log/fod && chown www-data:www-data /var/log/fod

COPY gunicorn.fod /etc/gunicorn.d/fod
COPY default.celeryd /etc/default/celeryd
COPY apache2.fod /etc/apache2/sites-available/fod
COPY flowspy.settings.py /srv/flowspy/flowspy/settings.py

RUN a2enmod rewrite && \
    a2enmod proxy && \
    a2enmod ssl && \
    a2enmod proxy_http && \
    a2enmod shib2 && \
    a2dissite default && \
    a2ensite fod

COPY docker-entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 80
CMD ["/bin/bash"]
