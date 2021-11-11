FROM centos:7 

MAINTAINER Eduardo Gonzalez Gutierrez <dabarren@gmail.com>

RUN yum install -y https://repos.fedorapeople.org/repos/openstack/openstack-mitaka/rdo-release-mitaka-3.noarch.rpm

RUN yum update -y

RUN yum -y install \
        openstack-rally \
        gcc \
        libffi-devel \
        python-devel \
        openssl-devel \
        gmp-devel \
        libxml2-devel \
        libxslt-devel \
        postgresql-devel \
        redhat-rpm-config \
        wget \
        openstack-selinux \
        openstack-utils && \ 
        yum clean all

RUN rally-manage --config-file /etc/rally/rally.conf db recreate
