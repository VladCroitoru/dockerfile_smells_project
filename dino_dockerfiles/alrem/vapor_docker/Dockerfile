FROM python:2
MAINTAINER Oleksandr Kosse <okosse@mirantis.com>

RUN  apt-get update -qq &&  \
apt-get install -q -y \
    python-dev \
    libvirt-dev && \
pip install pdbpp && \
apt-get clean  && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /opt/

ENV K_PARAM="not destructive"

RUN pip install -r https://raw.githubusercontent.com/openstack/fuel-plugin-contrail/master/plugin_test/vapor/requirements.txt

COPY entrypoint.sh /opt/

ENTRYPOINT ["/opt/entrypoint.sh"]
