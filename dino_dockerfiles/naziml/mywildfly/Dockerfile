FROM jboss/wildfly:latest
USER root
RUN yum -y update && yum -y install httpd && yum -y install rsync && yum -y install openssh-server && yum clean all 
RUN rm -rf /opt/jboss/wildfly/standalone/deployments/* && rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history 

RUN echo "root:Docker!" | chpasswd && /usr/bin/ssh-keygen -A
RUN mkdir -p ~/.ssh && touch ~/.ssh/authorized_keys && chown -R root:root ~/.ssh && chmod -R 700 ~/.ssh 
COPY sshd_config /etc/ssh/
RUN chown root:root /etc/ssh/sshd_config

COPY httpd.conf /etc/httpd/conf
RUN chown root:root /etc/httpd/conf/httpd.conf
ADD customisation /opt/jboss/wildfly/customisation
RUN chown -R jboss:root /opt/jboss/wildfly/customisation
EXPOSE 2222 80
ENTRYPOINT /opt/jboss/wildfly/customisation/startup.sh
