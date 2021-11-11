FROM centos:6.9

ENV container docker

RUN yum update -y \
 && yum groupinstall -y "Base" \
 && yum groupinstall -y "Development Tools" \
 && yum groupinstall -y "Emacs" \
 && yum groupinstall -y "Web Server" \
 && yum install -y \
  		curl \
		dstat \
		epel-release \
 		redhat-lsb \
 && yum clean all

EXPOSE 80

CMD ["/bin/bash"]
