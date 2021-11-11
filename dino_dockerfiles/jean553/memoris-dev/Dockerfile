# vim:set ft=dockerfile
FROM ubuntu:zesty

# install ansible
RUN apt-get update -y
RUN apt-get install -y \
    python-dev \
    python-pip \
    libssl-dev \
    libffi-dev

RUN pip install --upgrade \
    appdirs \
    packaging \
    ansible

# copy the provisioning folder
COPY provisioning/ provisioning

RUN \
    # run ansible
    ansible-playbook provisioning/site.yml -c local
