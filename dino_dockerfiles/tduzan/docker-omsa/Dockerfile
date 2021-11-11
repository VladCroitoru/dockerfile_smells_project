FROM centos:centos6

RUN yum update -y
RUN yum -y install perl openssl098e wget
RUN wget -q -O - http://linux.dell.com/repo/hardware/Linux_Repository_14.04.00/bootstrap.cgi | bash

RUN yum -y install srvadmin-all

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/dell/srvadmin/bin:opt/dell/srvadmin/sbin
