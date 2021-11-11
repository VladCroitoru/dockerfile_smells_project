
# biserver
FROM openshift/base-centos7

# TODO: Put the maintainer name in the image metadata
MAINTAINER George Tavares <tavares.george@gmail.com>

# TODO: Rename the builder environment variable to inform users about application you provide them
ENV BISERVER_VERSION 6.1

ENV BISERVER_TAG 6.1.0.1-196

# TODO: Set labels used in OpenShift to describe the builder image
#LABEL io.k8s.description="Platform for building xyz" \
#      io.k8s.display-name="builder x.y.z" \
#      io.openshift.expose-services="8080:http" \
#      io.openshift.tags="builder,x.y.z,etc."

# TODO: Install required packages here:
RUN yum install -y wget nano

#RUN wget http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm
#RUN rpm -ivh epel-release-7-8.noarch.rpm
RUN yum install -y supervisor java-1.8.0-openjdk java-1.8.0-openjdk-devel unzip

RUN yum clean all -y

RUN /usr/bin/wget --progress=dot:giga https://sourceforge.net/projects/pentaho/files/Business%20Intelligence%20Server/${BISERVER_VERSION}/biserver-ce-${BISERVER_TAG}.zip/download -O /tmp/biserver-ce-${BISERVER_TAG}.zip; \
    /usr/bin/unzip -q /tmp/biserver-ce-${BISERVER_TAG}.zip -d  $HOME; \
    rm -f /tmp/biserver-ce-${BISERVER_TAG}.zip $HOME/biserver-ce/promptuser.sh; \
    sed -i -e 's/\(exec ".*"\) start/\1 run/' $HOME/biserver-ce/tomcat/bin/startup.sh; \
    chmod +x $HOME/biserver-ce/start-pentaho.sh

RUN /usr/bin/wget --progress=dot:giga http://ufpr.dl.sourceforge.net/project/btable/Version2.1/BTable-pentaho5-STABLE-2.1.zip -O /tmp/plugin.zip ; \
    /usr/bin/unzip -q /tmp/plugin.zip -d  $HOME/biserver-ce/pentaho-solutions/system ; \
   rm /tmp/plugin.zip

RUN /usr/bin/wget --progress=dot:giga http://nexus.pentaho.org/content/groups/omni/pentaho/sparkl/6.1.0.1-196/sparkl-6.1.0.1-196.zip -O /tmp/plugin.zip ; \
    /usr/bin/unzip -q /tmp/plugin.zip -d  $HOME/biserver-ce/pentaho-solutions/system ; \
   rm /tmp/plugin.zip

RUN /usr/bin/wget --progress=dot:giga http://www.meteorite.bi/downloads/saiku-plugin-p6-3.8.8.zip -O /tmp/plugin.zip ; \
    /usr/bin/unzip -q /tmp/plugin.zip -d  $HOME/biserver-ce/pentaho-solutions/system ; \
   rm /tmp/plugin.zip


COPY scripts/start.sh ${HOME}/start.sh
RUN chmod +x ${HOME}/start.sh

COPY configs/license.lic $HOME/biserver-ce/pentaho-solutions/system/saiku/

COPY configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf



# TODO: Copy the S2I scripts to /usr/libexec/s2i, since openshift/base-centos7 image sets io.openshift.s2i.scripts-url label that way, or update that label
COPY ./.s2i/bin/ /usr/libexec/s2i

# TODO: Drop the root user and make the content of /opt/app-root owned by user 1001
RUN chown -R 1001:0 ${HOME} ; \
    chmod -R g+w ${HOME}

# This default user is created in the openshift/base-centos7 image
USER 1001

# TODO: Set the default port for applications built using this image
EXPOSE 8080

# TODO: Set the default CMD for the image
# CMD ["usage"]

#RUN sh ${HOME}/init-db.sh


CMD ["/opt/app-root/src/start.sh"]

