FROM centos/httpd-24-centos7

ENV SUMMARY="Ansible Container Documentation" \
    DESCRIPTION="Ansible Container Documentation as it seen in https://docs.ansible.com/ansible-container/. \
The image is based on centos/httpd-24-centos7 to run unprivileged httpd container."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="Ansible Container Documentation" \
      io.openshift.expose-services="8080:http,8443:https" \
      io.openshift.tags="documentation,docs,ansible-container-docs" \
      name="genadipost/dockerized-docs-ansible-container" \
      maintainer="Genadi Postrilko <genadipost@gmail.com>"

USER root

RUN yum -y install git python-pip && \
    pip install pyyaml sphinx

USER default

RUN git clone https://github.com/ansible/ansible-container

WORKDIR ansible-container/docs

RUN /bin/make html && \
    mv _build/html/* /var/www/html/

CMD ["/usr/bin/run-httpd"]
