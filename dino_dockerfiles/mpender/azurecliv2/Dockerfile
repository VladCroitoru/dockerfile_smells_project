FROM mpender/ansible-docker

RUN yum install -y gcc libffi-devel python-devel openssl-devel epel-release jq
RUN yum install python-pip -y
RUN pip install --user azure-cli

ENV PATH=$PATH:/root/.local/bin

ENTRYPOINT ["az"]

