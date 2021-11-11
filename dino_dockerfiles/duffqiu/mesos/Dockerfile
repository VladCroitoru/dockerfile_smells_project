FROM duffqiu/dockerjdk7:latest
MAINTAINER duffqiu@gmail.com

RUN yum install -y wget

# install mesos from mesosphere
RUN rpm -Uvh http://repos.mesosphere.io/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm
RUN yum -y install mesos

#install python tools including easy_install
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python

#install mesos egg
RUN wget http://downloads.mesosphere.io/master/centos/7/mesos-0.22.0-py2.7-linux-x86_64.egg -O mesos.egg

RUN easy_install --allow-hosts pypi.python.org mesos.egg

RUN rm -rf mesos.egg
RUN rm -rf setuptools-15.0.zip

RUN ln -sfn /usr/java/jdk1.7.0_79/jre/lib/amd64/server/libjvm.so /usr/lib/libjvm.so

ENTRYPOINT [ "/bin/bash", "-c" ]
