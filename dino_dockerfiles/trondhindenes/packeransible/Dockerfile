FROM ubuntu
RUN apt-get update
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get install git python-setuptools python-dev sshpass libffi-dev libssl-dev make libxml2-dev libxslt1-dev acl build-essential unzip wget -y
RUN easy_install pip
RUN pip install paramiko PyYAML jinja2 httplib2 requests lxml cssselect xmltodict
RUN pip install pywinrm
RUN pip install requests --upgrade
RUN pip install packaging
RUN pip install ansible==2.2.0
RUN wget https://releases.hashicorp.com/packer/1.0.0/packer_1.0.0_linux_amd64.zip
RUN unzip packer_1.0.0_linux_amd64.zip
RUN rm packer_1.0.0_linux_amd64.zip
RUN chmod +x packer
RUN cp packer /usr/bin

