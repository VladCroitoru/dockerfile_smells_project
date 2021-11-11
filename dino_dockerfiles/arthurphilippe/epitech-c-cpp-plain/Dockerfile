FROM fedora:28

LABEL version="2"
ADD install_criterion.sh /root/

RUN dnf -y update && dnf -y install gcc gcc-c++ wget bzip2 tar git openssh make gcovr cmake findutils unzip\
	&& dnf clean all \
	&& /root/install_criterion.sh \
	&& rm -fr /root/*

CMD bash
