FROM centos:7 

MAINTAINER Eduardo Gonzalez Gutierrez <dabarren@gmail.com>

RUN yum install -y https://repos.fedorapeople.org/repos/openstack/openstack-mitaka/rdo-release-mitaka-3.noarch.rpm

RUN yum update -y

RUN yum -y install \
        python-openstackclient \
        python-novaclient \
        python-keystoneclient \
        python-glanceclient \
        python-neutronclient \
        python-heatclient \
        python-ceilometerclient \
        python-troveclient \
        python-cinderclient \
        python-devel \
        openssl-devel \
        postgresql-devel \
        redhat-rpm-config \
        wget \
        openstack-selinux \
        MySQL-python \
	mariadb \
        openstack-utils && \ 
        yum clean all
COPY adminrc.sh /root/adminrc.sh
