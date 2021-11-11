FROM centos:7

RUN yum install -y epel-release
RUN yum install -y python python-pip gcc python-devel libffi-devel openssl openssl-devel
RUN pip install python-glanceclient==1.1.0
ENTRYPOINT ["glance"]
CMD ["--version"]
