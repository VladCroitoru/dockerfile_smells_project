FROM ubuntu:16.04
WORKDIR /tmp
RUN apt-get update
RUN apt-get install -fy git libffi-dev libssl-dev software-properties-common curl build-essential
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update
RUN apt-get install -fy python3.6 python3.6-dev
RUN curl -s https://bootstrap.pypa.io/get-pip.py | python3.6
RUN pip3.6 install setuptools
RUN git clone --branch v2.4.2.0-0.5.rc1 --depth 1 'https://github.com/ansible/ansible.git'
WORKDIR /tmp/ansible/
RUN python3.6 setup.py install
WORKDIR /tmp/
RUN rm -fr ansible
RUN git clone --branch 2.10 --depth 1 https://github.com/pallets/jinja.git
WORKDIR /tmp/jinja
RUN python3.6 setup.py install
WORKDIR /tmp/
RUN rm -fr jinja
WORKDIR /usr/local/share
RUN git clone --branch v2.4.0 --depth 1 https://github.com/kubernetes-incubator/kubespray
RUN apt-get install -fy python3-netaddr
VOLUME /usr/local/share/kubespray
WORKDIR /usr/local/share/kubespray
CMD /bin/bash -i
