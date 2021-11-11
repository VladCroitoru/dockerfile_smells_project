FROM centos:7 

MAINTAINER Neil Piper <neil.piper@gmail.com>

ENV MULE_EE_VERSION 3.8.4
ENV MULE_HOME /opt/mule

ARG GIT_COMMIT

ENV LOCAL_TIMEZONE=Australia/Melbourne

# install basic tools and set AE(D)ST timezone
RUN yum -y update && \
    yum install -y --skip-broken \
        iproute \
        curl \
        ruby \
        tar \
        wget \
        bind-utils \
        telnet \
        unzip && \
    yum clean all && \
    rm /etc/localtime && \
    ln -s /usr/share/zoneinfo/${LOCAL_TIMEZONE} /etc/localtime

# add the dumb-init binary
ENV DUMB_INIT_VERSION 1.2.0
RUN wget -O /usr/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v${DUMB_INIT_VERSION}/dumb-init_${DUMB_INIT_VERSION}_amd64 && \
    chmod +x /usr/bin/dumb-init

ENV JAVA_VERSION 1.8.0

RUN yum update && \
    yum install -y java-"${JAVA_VERSION}"-openjdk-headless && \
    yum clean all

ENV JAVA_HOME /usr/lib/jvm/jre-${JAVA_VERSION}-openjdk/

#COPY mule-ee-distribution-standalone-${MULE_EE_VERSION}.tar.gz .
# download, extract symlink, trim down mule EE distribution and then remove the downloaded archive
RUN curl -l -O http://s3.amazonaws.com/new-mule-artifacts/mule-ee-distribution-standalone-${MULE_EE_VERSION}.tar.gz && tar -zxvf mule-ee-distribution-standalone-${MULE_EE_VERSION}.tar.gz && \
    mv mule-enterprise-standalone-${MULE_EE_VERSION} /opt/mule-enterprise-standalone-${MULE_EE_VERSION} && \
    ln -s /opt/mule-enterprise-standalone-${MULE_EE_VERSION} ${MULE_HOME} && \
    rm mule-ee-distribution-standalone-${MULE_EE_VERSION}.tar.gz && \
    rm -rf ${MULE_HOME}/apps/default ${MULE_HOME}/docs ${MULE_HOME}/examples ${MULE_HOME}/src

ADD mule/conf/* ${MULE_HOME}/conf/
ADD mule/agent/* ${MULE_HOME}/conf/

ADD mule/lib/user/* ${MULE_HOME}/lib/user/
RUN mkdir -p /mnt/mule/conf

# java memory settings
ENV MULE_MEMORY_MIN_HEAP 128
ENV MULE_MEMORY_MAX_HEAP 512

ENV PATH $PATH:${MULE_HOME}/bin

# VOLUME ${MULE_HOME}/logs

# $MULE_HOME/.mule volume (ORDER IS IMPORTANT)
RUN useradd 1001 && usermod -a -G root 1001
RUN mkdir -m 0775 $MULE_HOME/.mule && \
	chown 1001:root $MULE_HOME/.mule && \
	chgrp -R -H 0 $MULE_HOME/.mule
VOLUME ${MULE_HOME}/.mule

# Support Arbitrary User IDs
# The following directives allow users in the root group 
# to access Files in the built image. Note that the order 
# in which the volumes are mounted is important for this to
# work (see above)
#
# NOTE: The root group does not have any special permissions 
# (unlike the root user) so there are no security concerns 
# with this arrangement. See:
#  https://docs.openshift.com/container-platform/3.3/creating_images/guidelines.html#openshift-container-platform-specific-guidelines

RUN chgrp -R -H 0 $MULE_HOME
RUN chgrp -R -H 0 /tmp
RUN chmod -R ug+rwx $MULE_HOME && \
	chmod -R ug+rwx $MULE_HOME/bin && \
	chmod -R ug+rwx $MULE_HOME/logs && \
	chmod -R ug+rwx $MULE_HOME/conf && \
	chmod -R ug+rwx /tmp && \
	chmod -R ug+rwx /mnt/mule
RUN find $MULE_HOME -type d -exec chmod -R g+x {} +
RUN chown -R 1001:0 $MULE_HOME && \
	chown -R 1001:0 $MULE_HOME/bin && \
	chown -R 1001:0 $MULE_HOME/logs && \
	chown -R 1001:0 $MULE_HOME/conf && \
	chown -R 1001:0 /tmp && \
	chown -R 1001:0 /mnt/mule

ADD start.sh /
RUN chmod +x /start.sh

VOLUME /mnt/mule/conf

#Switch to non-root user
USER 1001

LABEL git_commit ${GIT_COMMIT:-unknown}

#create dir for ssl certs and private keys
# RUN mkdir -p /etc/ssl
# VOLUME /etc/ssl

# this MULE_MANAGEMENT_JMX_PORT should be explicitly set in the properties files
ENV MULE_MANAGEMENT_JMX_PORT 1616

# port for jolokia agent
EXPOSE 8778

# Dumb-init is installed in the base centos7 image
# Runs "/usr/bin/dumb-init --rewrite 15:2 /start.sh"
# SIGTERM (15) to SIGINT (2)
ENTRYPOINT ["/usr/bin/dumb-init", "--rewrite", "15:2", "--"]
CMD ["/start.sh"]
