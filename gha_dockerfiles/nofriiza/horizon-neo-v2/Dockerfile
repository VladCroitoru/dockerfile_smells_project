FROM ubuntu:18.04

ENV HORIZON_BASEDIR=/opt/horizon \
    LANG=C \
    VERSION="stable/ussuri"

COPY . ${HORIZON_BASEDIR}
WORKDIR ${HORIZON_BASEDIR} 

RUN apt-get update && \
    apt-get install -y --no-install-recommends apt-utils  \
    apt-transport-https ca-certificates curl software-properties-common \
    gcc python3-minimal python3 python3-dev python3-pip python3-venv \ 
    python3-wheel python3-setuptools \ 
    git wget gettext nano libpcre3-dev libpcre++-dev libyaml-dev \
    apache2 libapache2-mod-wsgi-py3

RUN cd ${HORIZON_BASEDIR} && \
    #pip3 install --upgrade --user pip && \
    python3 -m pip install --user pip==21.0.1 && \
    python3 -m pip install . && \
    python3 -m pip install python-memcached && \
    python3 -m pip install oslo-log && \
    python3 -m pip install uwsgi && \
    cp openstack_dashboard/local/local_settings.py.dev openstack_dashboard/local/local_settings.py && \
    git clone -b ${VERSION} https://github.com/efenfauzi/heat-dashboard.git && \
    python3 -m pip install -e ./heat-dashboard/ && \
    cp heat-dashboard/heat_dashboard/enabled/* ${HORIZON_BASEDIR}/openstack_dashboard/local/enabled && \
    cp heat-dashboard/heat_dashboard/conf/* ${HORIZON_BASEDIR}/openstack_dashboard/conf/ && \
    cp heat-dashboard/heat_dashboard/local_settings.d/* ${HORIZON_BASEDIR}/openstack_dashboard/local/local_settings.d/ && \
    git clone -b stable/stein https://github.com/openstack/neutron-lbaas-dashboard.git && \
    cd neutron-lbaas-dashboard && \
    python3 setup.py sdist && \
    python3 setup.py install && \
    cp neutron_lbaas_dashboard/enabled/* ${HORIZON_BASEDIR}/openstack_dashboard/local/enabled/ && \
    python3 ./manage.py collectstatic --noinput && \
    python3 ./manage.py compress --force && \
    cd ${HORIZON_BASEDIR} && \
    python3 ./manage.py compilemessages && \
    python3 ./manage.py collectstatic --noinput && \
    python3 ./manage.py compress --force && \
    python3 ./manage.py make_web_conf --wsgi --force && \
    python3 ./manage.py make_web_conf --apache --force > /etc/apache2/sites-available/horizon.conf && \
    python3 -m compileall $HORIZON_BASEDIR

EXPOSE 80
RUN a2ensite horizon && \
    rm -rf /etc/apache2/sites-available/000-default.conf && \ 
    chown -R www-data:www-data /opt/horizon/openstack_dashboard/local && \
    chown -R www-data:www-data /var/tmp && \
    ln -sf /proc/self/fd/1 /var/log/apache2/openstack_dashboard-error.log

CMD ["/bin/bash", "entrypoint.sh"]
