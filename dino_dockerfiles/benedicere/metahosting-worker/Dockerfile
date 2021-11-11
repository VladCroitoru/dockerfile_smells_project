FROM centos:latest
MAINTAINER BeneDicere
RUN rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-5.noarch.rpm && yum -y update && yum install -y python python-pip git && yum clean all && rm -rf /var/lib/{yum,rpm}
RUN mkdir /app
ADD . /app/
WORKDIR /app
RUN pip install -r requirements.txt && \
    pip install --upgrade git+https://github.com/BeneDicere/metahosting-common
CMD /app/run.py --config config.ini