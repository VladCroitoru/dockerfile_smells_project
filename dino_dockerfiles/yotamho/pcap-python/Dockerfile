FROM centos

USER root

RUN yum -y update; yum clean all
RUN yum -y install epel-release; yum clean all
RUN yum -y install python-pip; yum clean all
RUN yum -y install libpcap-devel; yum clean all
RUN yum -y install wireshark; yum clean all
RUN yum -y install git; yum clean all

RUN yum -y install python-devel; yum clean all
RUN yum group install -y "Development Tools"
RUN wget -P /tmp http://downloads.sourceforge.net/project/pylibpcap/pylibpcap/0.6.4/pylibpcap-0.6.4.tar.gz
RUN tar xvf /tmp/pylibpcap-0.6.4.tar.gz -C /opt/
WORKDIR /opt/pylibpcap-0.6.4/
RUN ./setup.py install

RUN pip install --upgrade pip
RUN pip install pyshark psycopg2 dpkt
