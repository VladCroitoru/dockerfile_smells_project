FROM centos:6
MAINTAINER "lennardcornelis@gmail.com"
ENV container docker
RUN yum -y install epel-release wget; \
yum clean all
RUN yum -y install R
RUN wget https://raw.githubusercontent.com/chiefware/cranrepo6/master/cran.cmd -O cran.cmd
