FROM centos:centos7
# or, for example, FROM ansible/ubuntu14.04-ansible:stable

RUN yum clean all && \
    yum -y install epel-release

RUN yum install -y ansible gcc openssh-clients sshpass python-devel libffi-devel openssl-devel python-pip git

RUN pip install --upgrade pip

RUN pip install shade

ENV ANSIBLE_HOST_KEY_CHECKING False

WORKDIR /data

# Remove this so we can run other commands
#ENTRYPOINT ["ansible"]

# default command if none
CMD ["ansible", "--help"]