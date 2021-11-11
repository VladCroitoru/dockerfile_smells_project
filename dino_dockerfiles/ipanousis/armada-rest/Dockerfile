FROM centos:centos7

RUN yum -y install https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm
RUN yum -y install python-pip gcc python-devel openssh sshpass openssh-clients libffi-devel openssl-devel
RUN pip install requests Flask docker-py PyYAML port-for flask-cors python-etcd
RUN pip install supervisor
RUN pip install --upgrade pip
RUN pip install --quiet https://storage.googleapis.com/archive.clusterhq.com/downloads/flocker/Flocker-0.3.2-py2-none-any.whl

RUN mkdir -p /var/log/supervisor
RUN mkdir -p /etc/supervisor/conf.d
RUN mkdir -p /etc/armada-rest

EXPOSE 5000

VOLUME /etc/armada-rest

ADD . /app
ADD etc /etc

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
