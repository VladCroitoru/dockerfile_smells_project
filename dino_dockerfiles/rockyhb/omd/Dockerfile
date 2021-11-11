FROM centos:6
MAINTAINER Claas Rockmann-Buchterkirche <claas@rockbu.de>
EXPOSE 80 22 5666 6556
RUN rpm -Uvh "https://labs.consol.de/repo/testing/rhel6/i386/labs-consol-testing.rhel6.noarch.rpm"
RUN rpm -Uvh "https://dl.fedoraproject.org/pub/epel/epel-release-latest-6.noarch.rpm"
RUN yum clean all
RUN yum -y update
RUN yum -y install omd which lsof xinetd check-mk-agent git openssh-server
RUN omd create prod || true
RUN omd config prod set TMPFS off
RUN echo "omd" | passwd --stdin root
RUN echo "omd" | passwd --stdin prod
RUN chage -d 0 root
RUN chage -d 0 prod
RUN echo Done.
CMD /bin/bash
