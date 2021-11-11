FROM ubuntu:xenial
ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true
RUN locale-gen en_US.UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8

RUN apt-get update && \
apt-get upgrade -y && \
apt-get -y install software-properties-common && \
apt-add-repository ppa:ansible/ansible && \
apt-get update && \
apt-get install -y ansible && \
apt-get remove -y --purge software-properties-common && \
apt-get autoremove -y && \
apt-get clean && \
apt-get autoclean && \
rm -rf /var/lib/apt/lists/*

CMD ["/bin/bash"]
