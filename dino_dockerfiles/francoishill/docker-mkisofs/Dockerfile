FROM centos:7
MAINTAINER Francois Hill <francoishill11@gmail.com>

RUN yum -y install genisoimage 
RUN yum -y update; yum clean all

CMD ["/usr/bin/mkisofs", "--help"]
