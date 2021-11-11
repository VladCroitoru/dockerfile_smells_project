FROM rancher/jenkins-swarm:v0.2.0

USER root
ADD rancher-compose /usr/bin/rancher-compose
RUN chmod +x /usr/bin/rancher-compose
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y libssl-dev libffi-dev python-dev python-pip ca-certificates && \
    apt-get clean
RUN pip install --upgrade git+git://github.com/ansible/ansible.git@devel
RUN update-ca-certificates -f

USER jenkins
WORKDIR /var/jenkins_home

ENTRYPOINT ["/run.sh"]
