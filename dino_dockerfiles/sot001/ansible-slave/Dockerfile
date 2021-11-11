# pull base image
FROM jenkinsci/jnlp-slave:latest

USER root

RUN echo "===> Adding Ansible's prerequisites..."   && \
    DEBIAN_FRONTEND=noninteractive  \
    apt-get update -y            && \
        apt-get install --no-install-recommends -y -q  \
                build-essential                        \
                python-pip python-dev python-yaml      \
                libffi-dev libssl-dev                  \
                libxml2-dev libxslt1-dev zlib1g-dev    \
                git software-properties-common      && \
    pip install --upgrade wheel setuptools          && \
    pip install --upgrade pyyaml jinja2 pycrypto    && \
    echo 'deb http://http.debian.net/debian jessie-backports main' > /etc/apt/sources.list.d/backports.list  && \
    DEBIAN_FRONTEND=noninteractive  \
    apt-get update -y            && \
    DEBIAN_FRONTEND=noninteractive  \
    apt-get -t jessie-backports install "ansible" -y -q && \
    DEBIAN_FRONTEND=noninteractive  \
    apt-get dist-upgrade -o Dpkg::Options::="--force-confold" -o Dpkg::Options::="--force-confdef" -y -q && \
    DEBIAN_FRONTEND=noninteractive  \
    apt-get autoremove -y


# push across any ssh stuff
ADD ssh .ssh
RUN chmod 700 .ssh
RUN chown -R jenkins:jenkins .ssh
RUN pip install awscli boto boto3

USER jenkins

ENV PATH        /opt/ansible/bin:$PATH
ENV PYTHONPATH  /opt/ansible/lib:$PYTHONPATH
ENV MANPATH     /opt/ansible/docs/man:$MANPATH
ENV SHELL       /bin/bash


# default command: display Ansible version
#ENTRYPOINT [ "ansible-playbook", "--version" ]
ENTRYPOINT ["jenkins-slave"]
