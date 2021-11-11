FROM centos:centos7

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ceph.repo /etc/yum.repos.d/ceph.repo

RUN yum install -y epel-release && \
    yum install -y python python-pip python-flask python-gunicorn && \
    yum install -y ceph && \
    yum clean all -y

RUN pip install dpath flask-wtf

RUN curl -L https://github.com/openshift/origin/releases/download/v1.3.0/openshift-origin-client-tools-v1.3.0-3ab7af3d097b57f933eccef684a714f2368804e7-linux-64bit.tar.gz | tar -xz && \
    mv openshift*/oc /usr/local/bin && \
    rm -rf openshift-origin-client-tools-*

EXPOSE 5000

COPY . /usr/src/app

CMD oc project default && gunicorn --bind 0.0.0.0:5000 --workers 10 wsgi:app
