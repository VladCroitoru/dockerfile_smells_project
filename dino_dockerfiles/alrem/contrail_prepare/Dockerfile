FROM ubuntu
MAINTAINER Oleksandr Kosse <okosse@mirantis.com>

RUN  apt-get update -qq &&  \
apt-get install -q -y \
    ansible \
    python-pip && \
sed -ie 's/#host_key_checking/host_key_checking/g' /etc/ansible/ansible.cfg && \
pip install python-openstackclient pip --upgrade && \
apt-get clean  && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ENV ROUTER_IP="10.167.4.100"
ENV EXT_NET="172.17.35.64/26"

COPY entrypoint.sh /opt/

ENTRYPOINT ["/opt/entrypoint.sh"]