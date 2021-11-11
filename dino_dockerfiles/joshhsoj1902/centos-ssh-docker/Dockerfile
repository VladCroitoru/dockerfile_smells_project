FROM jdeathe/centos-ssh:latest@sha256:68a64b81241322d960be61d787b0e360008fe7ab358e00ed07b6cbb287e8e422

RUN yum install -y vim

RUN yum install -y wget \
 && wget -qO- https://get.docker.com/ | sh \
 && systemctl enable docker.service

RUN yum install -y python-pip \
 && pip install docker-compose