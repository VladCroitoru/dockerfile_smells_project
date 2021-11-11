FROM centos:7
RUN useradd -ms /bin/bash centos
RUN yum -y install python-devel sshpass gcc git libffi-devel \
    libxml2-devel libxslt-devel  mariadb-devel openssl-devel  python-pip \
    python-virtualenv  redhat-rpm-config sudo iputils wget \
    vim
RUN yum -y update && mkdir -p /etc/tempest

RUN echo "centos ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
ADD scripts /home/centos/scripts
RUN chmod 755 -R /home/centos/scripts \
    && chown centos:centos /home/centos/scripts

USER centos
WORKDIR /home/centos
RUN virtualenv tempest-upstream && cd tempest-upstream \
    && source bin/activate \
    && git clone https://github.com/openstack/python-tempestconf.git ; cd python-tempestconf \
    && pip install -U pip python-subunit && pip install -U setuptools  \
    && pip install requests && pip install -r requirements.txt \
    && cd .. \
    && git clone https://github.com/openstack/tempest.git && cd tempest \
    && pip install -r test-requirements.txt \
    && pip install ipdb python-openstackclient && cd .. \

WORKDIR /home/centos/tempest-upstream/tempest
RUN wget http://download.cirros-cloud.net/0.3.4/cirros-0.3.4-x86_64-disk.img -P etc
CMD ['/bin/bash']
