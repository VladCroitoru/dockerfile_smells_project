      FROM alpine:edge
      MAINTAINER Mateusz Pawlowski 
      RUN apk --update add \
        py-yaml py-jinja2  py-paramiko py-setuptools git py-pip perl py-simplejson rsync \
      && apk add py-httplib2 py-netifaces py-msgpack openssh \
         --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
      && rm -rf /var/cache/apk/*
      RUN pip install python-novaclient python-keyczar boto
      RUN mkdir /etc/ansible/
      RUN echo "[local]" > /etc/ansible/hosts ; echo "localhost" >> /etc/ansible/hosts
      RUN mkdir /opt/ansible/ -p
      RUN git clone http://github.com/ansible/ansible.git /opt/ansible/ansible
      WORKDIR /opt/ansible/ansible
      RUN git checkout stable-2.0.0.1
      RUN git submodule update --init
      ENV PATH /opt/ansible/ansible/bin:/bin:/usr/bin:/sbin:/usr/sbin
      ENV PYTHONPATH /opt/ansible/ansible/lib
      ENV ANSIBLE_LIBRARY /opt/ansible/ansible/library
      RUN mkdir /ansible
      WORKDIR /ansible

