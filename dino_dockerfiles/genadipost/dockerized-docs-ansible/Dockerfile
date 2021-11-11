FROM centos/httpd-24-centos7

ENV SUMMARY="Ansible Documentation" \
    DESCRIPTION="Ansible Documentation as it seen in http://docs.ansible.com/ansible/latest/intro.html. \
The image is based on centos/httpd-24-centos7 to run unprivileged httpd container."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="Ansible Documentation" \
      io.openshift.expose-services="8080:http,8443:https" \
      io.openshift.tags="documentation,docs,ansible-docs" \
      name="genadipost/dockerized-docs-ansible" \
      release="2" \
      maintainer="Genadi Postrilko <genadipost@gmail.com>"

USER root

RUN yum -y install git python-pip && \
    pip install pyyaml sphinx

USER default

RUN git clone https://github.com/ansible/ansible --recursive

WORKDIR ansible

RUN /bin/make webdocs && \
    mv docs/docsite/_build/html/* /var/www/html/

CMD ["/usr/bin/run-httpd"]
