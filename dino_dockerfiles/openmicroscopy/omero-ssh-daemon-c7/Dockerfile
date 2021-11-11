FROM centos:centos7
MAINTAINER ome-devel@lists.openmicroscopy.org.uk

RUN yum install -y sudo openssh-server openssh-clients && \
	yum clean all

RUN sed -i \
	's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' \
	/etc/pam.d/sshd && \
	/usr/bin/ssh-keygen -q -t rsa -f /etc/ssh/ssh_host_rsa_key \
	-C '' -N ''

# To avoid error: sudo: sorry, you must have a tty to run sudo
RUN sed -i -e "s/Defaults    requiretty.*/ #Defaults    requiretty/g" /etc/sudoers

RUN useradd omero && \
	echo 'omero:omero' | chpasswd omero &&\
	echo "omero ALL= (ALL) NOPASSWD: ALL" >> /etc/sudoers.d/omero

EXPOSE 22

CMD ["/usr/sbin/sshd", "-eD"]
