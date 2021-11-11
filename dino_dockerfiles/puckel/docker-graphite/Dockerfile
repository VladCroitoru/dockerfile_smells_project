# VERSION 2.0
# AUTHOR: Matthieu "Puckel_" Roisil
# DESCRIPTION: Basic Graphite container
# BUILD: docker build --rm -t puckel/docker-graphite
# SOURCE: https://github.com/puckel/docker-graphite

FROM puckel/docker-base
MAINTAINER Puckel_

# Never prompts the user for choices on installation/configuration of packages
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux
# Work around initramfs-tools running on kernel 'upgrade': <http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>
ENV INITRD No

ENV GRAPHITE_RELEASE 0.9.13-pre1
ENV GRAPHITE_HOME /opt/graphite
ENV GRAPHITE_CONF ${GRAPHITE_HOME}/conf
ENV GRAPHITE_WEBAPP ${GRAPHITE_HOME}/webapp
ENV GRAPHITE_STORAGE ${GRAPHITE_HOME}/storage

ADD config /root/config

RUN apt-get update -yqq \
    && apt-get install -yqq \
    libcairo2-dev libffi-dev pkg-config python-dev python-pip fontconfig apache2 libapache2-mod-wsgi git-core collectd memcached \
    gcc g++ make supervisor \
    build-essential libtool autoconf automake scons python-setuptools lsof git texlive check \
    && apt-get clean \
    && rm -rf \
    easy_install pip \
    pip install pytest \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base

RUN cd /usr/local/src \
    && git clone https://github.com/graphite-project/graphite-web.git \
    && git clone https://github.com/graphite-project/carbon.git \
    && git clone https://github.com/graphite-project/whisper.git \
    && git clone https://github.com/statsite/statsite.git \
    && cd whisper; git checkout ${GRAPHITE_RELEASE}; python setup.py install \
    && cd ../carbon; git checkout ${GRAPHITE_RELEASE}; pip install -r requirements.txt; python setup.py install \
    && cd ../graphite-web; git checkout ${GRAPHITE_RELEASE}; pip install -r requirements.txt; python check-dependencies.py; python setup.py install \
    && cd ../statsite; /bin/sh autogen.sh; /bin/sh configure; make; make install; cp statsite /usr/local/sbin/; cp sinks/graphite.py /usr/local/sbin/statsite-sink-graphite.py \
    && mkdir ${GRAPHITE_CONF}/examples \
    && mv ${GRAPHITE_CONF}/*.example ${GRAPHITE_CONF}/examples/ \
    && cp /root/config/statsite/statsite.conf /etc/statsite.conf \
    && cp /root/config/graphite/conf/* ${GRAPHITE_CONF}/ \
    && cp /root/config/graphite/webapp/* ${GRAPHITE_WEBAPP}/graphite/ \
    && sed -i -e "s/UNSAFE_DEFAULT/`date | md5sum | cut -d ' ' -f 1`/" ${GRAPHITE_WEBAPP}/graphite/local_settings.py \
    && cp /root/config/apache/*.conf /etc/apache2/sites-available/ \
    && cp /root/config/supervisor/*.conf /etc/supervisor/conf.d/graphite.conf \
    && cd ${GRAPHITE_WEBAPP}/graphite && python manage.py syncdb --noinput \
    && a2dissite 000-default \
    && a2ensite graphite \
    && a2enmod socache_shmcb rewrite \
    && chown www-data:www-data ${GRAPHITE_STORAGE}/graphite.db \
    && groupadd -g 998 carbon \
    && useradd -c "carbon user" -g 998 -u 998 -s /bin/false carbon \
    && chmod 775 ${GRAPHITE_STORAGE} \
    && chown www-data:carbon ${GRAPHITE_STORAGE} \
    && chown -R carbon ${GRAPHITE_STORAGE}/whisper \
    && mkdir ${GRAPHITE_STORAGE}/log/apache2 \
    && chown www-data ${GRAPHITE_STORAGE}/log/webapp \
    && cp /root/config/graphite/cron/build-index /etc/cron.hourly/graphite-build-index \
    && chmod 755 /etc/cron.hourly/graphite-build-index

EXPOSE 80 2003 2004 7002 8125

CMD ["/usr/bin/supervisord"]
