FROM centos:centos7

RUN yum install -y https://centos7.iuscommunity.org/ius-release.rpm && yum clean all
RUN yum groupinstall -y "Development tools" && yum clean all
RUN yum install -y python35u python35u-devel python35u-libs python35u-pip python35u-setuptools python35u-tools libffi-devel libxml2-devel libxslt-devel openssl-devel libjpeg-turbo-devel libpng-devel giflib-devel libtiff-devel && yum clean all
RUN pip3.5 install lxml
RUN pip3.5 install Pillow
RUN pip3.5 install libsass
RUN pip3.5 install greenlet
RUN pip3.5 install gevent
RUN pip3.5 install cryptography
RUN pip3.5 install ujson
RUN pip3.5 install bcrypt
RUN pip3.5 install cffi

