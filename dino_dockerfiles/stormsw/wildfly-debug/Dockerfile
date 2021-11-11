#!/usr/bin/docker
# based on Ubuntu
FROM stormsw/wildfly
MAINTAINER Alexander Varchenko <alexander.varchenko@gmail.com>
COPY datasource.cli /tmp/batch.cli
RUN /tmp/config.sh
USER root
# Fix for Error: Could not rename /opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current
#RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history
RUN mv /opt/jboss/wildfly/standalone/configuration/standalone_xml_history/current /opt/jboss/wildfly/standalone/configuration/standalone_xml_history/$(date +"%Y%m%d-%s")
USER jboss
# Expose the ports we're interested in
EXPOSE 8080 9990 8787
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "--debug", "8787", "-b", "0.0.0.0", "-bmanagement","0.0.0.0"]
