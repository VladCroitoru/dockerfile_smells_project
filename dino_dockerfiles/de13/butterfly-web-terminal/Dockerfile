FROM centos:7

MAINTAINER de13 <stephane.beuret@data-essential.com>

RUN yum install -y epel-release
RUN yum install -y python-setuptools python-dev python-pip gcc openssl openssl-devel python-devel
RUN pip install --upgrade pip && \
    pip install butterfly && \
    pip install libsass
COPY entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
