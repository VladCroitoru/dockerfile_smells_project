FROM loriss/centos-openstack-cli
MAINTAINER Predrag Knezevic <pedjak@gmail.com>

RUN yum makecache fast && \
	yum install -y qemu-img docker parted tar && \
	yum clean all 

ADD openstack2docker /usr/bin/openstack2docker
RUN chmod 755 /usr/bin/openstack2docker

ENTRYPOINT ["/usr/bin/openstack2docker"]


