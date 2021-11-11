FROM centos/httpd-24-centos7

ENV SUMMARY="Jinja Documentation" \
    DESCRIPTION="Jinja Documentation as it seen in http://jinja.pocoo.org/docs/. \
The image is based on centos/httpd-24-centos7 to run unprivileged httpd container."

LABEL summary="$SUMMARY" \
      description="$DESCRIPTION" \
      io.k8s.description="$DESCRIPTION" \
      io.k8s.display-name="Jinja Documentation" \
      io.openshift.expose-services="8080:http,8443:https" \
      io.openshift.tags="documentation,docs,jinja" \
      name="genadipost/dockerized-docs-jinja" \
      maintainer="Genadi Postrilko <genadipost@gmail.com>"

USER root

RUN yum -y install git python-pip && \
    pip install sphinx

USER default

RUN git clone https://github.com/pallets/jinja

WORKDIR jinja/docs

RUN /bin/make html && \
    mv _build/html/* /var/www/html/

CMD ["/usr/bin/run-httpd"]
