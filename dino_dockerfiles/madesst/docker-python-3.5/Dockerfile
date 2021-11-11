FROM centos:7

MAINTAINER madesst@gmail.com

RUN rpm --rebuilddb; yum install -y yum-plugin-ovl
RUN yum install epel-release -y && rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && rpm --import /etc/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY

RUN yum upgrade -y
RUN yum install -y gcc \
                   python35u-devel \
                   python35u-debug \
                   python35u-setuptools \
                   python35u-pip \
                   python35u-libs \
                   libevent-devel

RUN cd /usr/local/bin \
        && ln -s /usr/bin/easy_install-3.5 easy_install \
        && ln -s /usr/bin/pip3.5 pip \
        && ln -s /usr/bin/python3.5 python \
        && ln -s /usr/bin/python3.5-config python-config \
        && ln -s /usr/bin/python3.5-debug python-debug \
        && ln -s /usr/bin/pydoc3.5 pydoc \
        && ln -s /usr/bin/idle3.5 idle

COPY ./pycharm-debug-py3k.egg /pycharm-debug-py3k.egg
RUN pip install virtualenv

CMD ["/bin/bash"]
