FROM centos:latest
RUN sed -i '/tsflags=nodocs/d' /etc/yum.conf && \
	sed -i '/override_install_langs/d' /etc/yum.conf && \
	localedef -c -i en_US -f UTF-8 en_US.UTF-8 && \
	yum install -y man vim bash-completion git glib&& \
	yum group mark-install minimal compute-node-environment && \
	yum update -y && \
	yum reinstall -y $(yum list installed | awk '{ print $1 }')

