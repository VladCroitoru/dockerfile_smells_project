FROM solr:6.6
MAINTAINER  Jason Dudash "jason.dudash@gmail.com"

USER root
ENV STI_SCRIPTS_PATH=/usr/libexec/s2i

LABEL io.k8s.description="Run SOLR search in OpenShift" \
      io.k8s.display-name="SOLR 6.6" \
      io.openshift.expose-services="8983:http" \
      io.openshift.tags="builder,solr,solr6.6" \
      io.openshift.s2i.scripts-url="image:///${STI_SCRIPTS_PATH}"

COPY ./s2i/bin/. ${STI_SCRIPTS_PATH}
RUN chmod -R a+rx ${STI_SCRIPTS_PATH}

# If we need to add files as part of every SOLR conf, they'd go here
# COPY ./solr-config/ /tmp/solr-config

# Give the SOLR directory to root group (not root user)
# https://docs.openshift.org/latest/creating_images/guidelines.html#openshift-origin-specific-guidelines
RUN chgrp -R 0 /opt/solr \
  && chmod -R g+rwX /opt/solr

RUN chgrp -R 0 /opt/docker-solr \
  && chmod -R g+rwX /opt/docker-solr

USER 8983
