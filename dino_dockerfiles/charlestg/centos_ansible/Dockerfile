# https://github.com/ansible/ansible-docker-base

FROM ansible/centos7-ansible:stable
# or, for example, FROM ansible/ubuntu14.04-ansible:stable

# SOURCE install packages
#RUN yum clean all && \
#    yum -y install epel-release && \
#    yum -y install PyYAML python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools git python-pip

RUN yum install -y gcc openssh-clients sshpass python-devel libffi-devel openssl-devel

RUN pip install shade

ENV ANSIBLE_HOST_KEY_CHECKING False

WORKDIR /data

# Remove this so we can run other commands
#ENTRYPOINT ["ansible"]

# default command if none
CMD ["ansible", "--help"]
