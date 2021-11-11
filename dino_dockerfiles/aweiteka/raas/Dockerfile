FROM centos:7.0.1406
MAINTAINER Aaron Weitekamp <aweiteka@redhat.com>

RUN yum install -y http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-6.noarch.rpm
RUN yum install -y git python-pip ruby rubygems

ADD express.conf /root/.openshift/express.conf
ADD requirements.txt /root/raas/
ADD raas.py /root/raas/
ADD VERSION /root/
ADD LICENSE /root/

RUN pip install -r /root/raas/requirements.txt
RUN pip install awscli
RUN gem install rhc

ADD pulp.repo /etc/yum.repos.d/pulp.repo
RUN yum groupinstall -y pulp-admin
RUN yum install -y pulp-docker-admin-extensions

ADD init.sh /root/init.sh
RUN ln -s /root/raas/raas.py /usr/bin/raas
RUN ln -s /root/init.sh /usr/bin/init

CMD ["bash"]

