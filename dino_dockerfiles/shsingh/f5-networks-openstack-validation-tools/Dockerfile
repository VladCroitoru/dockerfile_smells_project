FROM centos:7.3.1611
MAINTAINER John Gruber "j.gruber@f5.com"

# add the CentOS Mitaka repo as a starting point
RUN yum -y install centos-release-openstack-mitaka
RUN yum -y update
# install development tools for environment builds
RUN yum -y groups mark install "Development Tools"
RUN yum -y groups mark convert "Development Tools"
RUN yum -y groupinstall "Development Tools"
# install what we need for environemnt build and to 
# make the test client a good diagnostic tool.
RUN yum -y install ansible openssl-devel libffi libffi-devel python-devel git python-pip python-openstackclient python-heatclient

# update key python tools and libraries
RUN pip install --upgrade pip setuptools virtualenv tempest ipython

# add interesting f5 tools
RUN git clone -b mitaka https://github.com/F5Networks/f5-openstack-agent.git
RUN pip install /f5-openstack-agent/
RUN rm -rf /f5-openstack-agent

# copy init environment functions
COPY init-functions ./
COPY environments/ /environments/

# Uncomment the ENV setting to enable specific testing environments

# test that neutron has extension to support F5 LBaaS and other multi-tenant service
ENV enable_validate_neutron_for_f5_services=1

# test neutron in a liberty openstack cloud
ENV enable_neutron_liberty=1

# test neutron lbaasv2 in a liberty openstack cloud 
ENV enable_lbaasv2_liberty=1

# test neutron in a mitaka openstack cloud
ENV enable_neutron_mitaka=1

# test neutron lbaasv2 in a mitaka openstack cloud 
ENV enable_lbaasv2_mitaka=1

# test neutron in a newton openstack cloud
 ENV enable_neutron_newton=1

# test neutron lbaasv2 in a newton openstack cloud 
 ENV enable_lbaasv2_newton=1

# test neutron in a ocata openstack cloud
 ENV enable_neutron_ocata=1

# test neutron lbaasv2 in a ocata openstack cloud 
 ENV enable_lbaasv2_ocata=1

# create TMOS Virtual Edition images for OpenStack
ENV enable_image_importer=1

# create Nova Flavor for TMOS Virtual Editions
ENV enable_f5_nova_flavors=1

RUN /environments/install.sh

WORKDIR /
# run interactively
CMD /bin/bash 
