FROM debian:jessie
MAINTAINER Christian Simon <simon@swine.de>

RUN apt-get update &&  \
    DEBIAN_FRONTEND=noninteractive apt-get -y install curl build-essential python-pip \
    python-dev libyaml-dev nano openssh-client && \
    apt-get clean && \
    rm /var/lib/apt/lists/*_*

RUN groupadd -g 950 ansible && \
    useradd -u 950 -g 950 -d /ansible ansible

WORKDIR /ansible/code
COPY requirements.txt /ansible/code/
RUN pip install -r requirements.txt
RUN chown -cR ansible:ansible /ansible
RUN chown -cR ansible:ansible /ansible

USER ansible

# download kubespray's code
ENV K8S_CONTRIB_VERSION 41772990cb22173c8a69d161966b1a87dec2eafb
RUN curl -L https://github.com/kubernetes/contrib/archive/${K8S_CONTRIB_VERSION}.tar.gz | \
    tar xzvf - contrib-${K8S_CONTRIB_VERSION}/ansible/ --strip-components=2

COPY run.py /ansible/run.py
COPY ansible/ansible.cfg /ansible/code/
COPY ansible/group_vars/coreos.yml /ansible/code/group_vars/coreos.yml

# TODO: remove me only for dev
COPY parameters.yaml /ansible/code/

USER root
RUN chown -cR ansible:ansible /ansible
USER ansible

ENTRYPOINT ["/usr/bin/python", "/ansible/run.py"]

CMD discover
