FROM jenkins
USER root
ADD rancher-compose /usr/bin/rancher-compose
RUN chmod +x /usr/bin/rancher-compose
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y libssl-dev libffi-dev python-dev python-pip && \
    apt-get clean
RUN pip install --upgrade git+git://github.com/ansible/ansible.git@devel
USER jenkins
