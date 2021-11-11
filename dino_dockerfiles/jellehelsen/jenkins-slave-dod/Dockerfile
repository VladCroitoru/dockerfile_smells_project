FROM jenkins/jnlp-slave

USER root

RUN apt-get update && apt-get -y install libltdl7 python-pip
RUN pip install ansible jmespath
RUN echo StrictHostKeyChecking no >> /etc/ssh/ssh_config

# Use tini as subreaper in Docker container to adopt zombie processes 
RUN curl -fL https://github.com/krallin/tini/releases/download/v0.5.0/tini-static -o /bin/tini && chmod +x /bin/tini

USER jenkins

ENTRYPOINT ["/bin/tini", "--", "/usr/local/bin/jenkins-slave"]
