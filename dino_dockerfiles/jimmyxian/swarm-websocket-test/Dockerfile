FROM centos:7

RUN yum -y install epel-release && yum -y update && yum clean all
RUN yum -y install python-pip && yum clean all

RUN pip install websocket_client==0.32

COPY ./wssh.py /usr/bin/wssh
RUN chmod +x /usr/bin/wssh
