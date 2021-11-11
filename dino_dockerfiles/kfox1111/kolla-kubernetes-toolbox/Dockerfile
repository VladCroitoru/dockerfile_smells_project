FROM centos:centos7
MAINTAINER Kevin Fox "Kevin.Fox@pnnl.gov"

RUN \
  rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm; \
  yum install -y git python-virtualenv python-devel gcc openssl-devel; \
  adduser kolla;

RUN \
  cd /; \
  su - kolla /bin/bash -c 'set -e; cd; git clone https://github.com/openstack/kolla.git; \
    cd kolla; \
    git config --global user.email "you@example.com"; \
    git config --global user.name "Your Name"; \
    virtualenv .venv; \
    . .venv/bin/activate; \
    pip install pip --upgrade; \
    pip install "ansible<2.1";\
    pip install -r requirements.txt; \
    pip install pyyaml; \
    cd ..; git clone https://github.com/openstack/kolla-kubernetes.git; \
    cd kolla-kubernetes; \
    pip install -r requirements.txt; \
    pip install .; echo force rebuild 1'

ADD start.sh /start.sh
ADD kolla_config /tmp/kolla_config
ADD kolla_kubernetes_config /tmp/kolla_kubernetes_config
ADD gen_keystone_admin.sh /home/kolla/gen_keystone_admin.sh
ADD openstackcli.yaml /home/kolla/openstackcli.yaml
ADD stash_config.sh /home/kolla/stash_config.sh
ADD set_external_ip.sh /home/kolla/set_external_ip.sh

RUN cat /tmp/kolla_config >> /home/kolla/kolla/etc/kolla/globals.yml
RUN cat /tmp/kolla_kubernetes_config >> /home/kolla/kolla-kubernetes/etc/kolla-kubernetes/kolla-kubernetes.yml

#FIXME... This should copy the files over if they are unchanged... md5sum
RUN ln -s /home/kolla/kolla-kubernetes/etc/kolla-kubernetes /etc/kolla-kubernetes

RUN ln -s /home/kolla/kolla /usr/share/kolla

RUN yum install -y jq wget sudo crudini

RUN sed -i 's/sudo//' /home/kolla/kolla-kubernetes/tools/setup-kubectl.sh; /home/kolla/kolla-kubernetes/tools/setup-kubectl.sh

RUN mkdir /etc/kolla; \
    chown kolla /etc/kolla; \
    mkdir /etc/kolla-kubernetes; \
    chown kolla /etc/kolla-kubernetes;

USER kolla

ENTRYPOINT ["/start.sh"]
CMD ["tools/kolla-ansible", "genconfig"]
