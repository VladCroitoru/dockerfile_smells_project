FROM amazonlinux:latest

WORKDIR /var/task

RUN curl --silent --location https://rpm.nodesource.com/setup_6.x | bash -
RUN yum update -y
RUN yum install -y gcc git libffi-devel openssl-devel nodejs python36 python36-devel python36-pip

CMD ["/bin/bash"]
