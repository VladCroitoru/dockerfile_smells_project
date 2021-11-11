FROM centos:7.2.1511
MAINTAINER Mark Goddard <mark@stackhpc.com>
RUN yum -y install \
    centos-release-openstack-newton \
    epel-release \
    && yum -y update
RUN yum -y install \
    ansible \
    python-dracclient \
    python-ironicclient \
    && yum -y update
RUN ansible-galaxy install \
    stackhpc.drac \
    stackhpc.drac-facts
COPY . /ansible-drac-examples
WORKDIR /ansible-drac-examples
CMD ["bash"]
