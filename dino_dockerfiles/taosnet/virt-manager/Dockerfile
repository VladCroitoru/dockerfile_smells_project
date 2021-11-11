FROM taosnet/vnc
MAINTAINER Chris Batis <clbatis@taosnet.com>

RUN yum update -y \
	&& yum install -y --setopt=tsflags=nodocs virt-manager matchbox-window-manager xterm openssh openssh-askpass abattis-cantarell-fonts openssh-clients \
	&& yum clean all

COPY wrapper.sh /wrapper.sh
CMD ["xterm", "-e", "/wrapper.sh"]
