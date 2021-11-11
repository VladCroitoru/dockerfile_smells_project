FROM fedora:latest
MAINTAINER Juan Manuel Parrilla Madrid <jparrill@redhat.com>
RUN cd $HOME
RUN dnf install -y git gcc libffi-devel python-devel openssl-devel gmp-devel libxml2-devel libxslt-devel postgresql-devel redhat-rpm-config wget python-pip which \
    && dnf clean all
RUN git clone https://github.com/openstack/rally.git
RUN ./rally/install_rally.sh
RUN mkdir -p /rally
WORKDIR /rally
CMD ["bash"]
