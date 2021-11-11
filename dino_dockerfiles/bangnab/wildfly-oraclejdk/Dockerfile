FROM centos:7
MAINTAINER Nicola Ambrosetti Brolin <ambrosetti.nicola@gmail.com>

# Install packages necessary to run EAP
RUN yum update -y && yum -y install wget xmlstarlet saxon augeas bsdtar unzip && yum clean all

# Create a user and group used to launch processes
# The user ID 1000 is the default for the first "regular" user on Fedora/RHEL,
# so there is a high chance that this ID will be equal to the current user
# making it easier to use volumes (no permission issues)
RUN groupadd -r jboss -g 1000 && useradd -u 1000 -r -g jboss -m -d /opt/jboss -s /sbin/nologin -c "JBoss user" jboss && \
    chmod 755 /opt/jboss

# Set the working directory to jboss' user home directory
WORKDIR /opt/jboss

# Install Oracle JDK
ENV JDK_SHA256 cdb016da0c509d7414ee3f0c15b2dae5092d9a77edf7915be4386d5127e8092f
ENV JDK_VERSION 8u144
ENV JDK_DIR 8u144-b01/090f390dda5b47b9b721c7dfaa008135

RUN curl -L -O -H "Cookie: oraclelicense=accept-securebackup-cookie" -k "http://download.oracle.com/otn-pub/java/jdk/${JDK_DIR}/jdk-${JDK_VERSION}-linux-x64.rpm" \
    && sha256sum jdk-${JDK_VERSION}-linux-x64.rpm | grep ${JDK_SHA256} \
    && yum localinstall -y jdk-${JDK_VERSION}-linux-x64.rpm \ 
    && rm jdk-${JDK_VERSION}-linux-x64.rpm 

# Switch back to jboss user
USER jboss

# Set the JAVA_HOME variable to make it clear where Java is located
ENV JAVA_HOME /usr/java/default

ENV WILDFLY_VERSION 10.1.0.Final
ENV WILDFLY_SHA1 9ee3c0255e2e6007d502223916cefad2a1a5e333
ENV JBOSS_HOME /opt/jboss/wildfly

# Add the WildFly distribution to /opt, and make wildfly the owner of the extracted tar content
# Make sure the distribution is available from a well-known place
RUN cd $HOME \
    && curl -O https://download.jboss.org/wildfly/$WILDFLY_VERSION/wildfly-$WILDFLY_VERSION.tar.gz \
    && sha1sum wildfly-$WILDFLY_VERSION.tar.gz | grep $WILDFLY_SHA1 \
    && tar xf wildfly-$WILDFLY_VERSION.tar.gz \
    && mv $HOME/wildfly-$WILDFLY_VERSION $JBOSS_HOME \
    && rm wildfly-$WILDFLY_VERSION.tar.gz

# Ensure signals are forwarded to the JVM process correctly for graceful shutdown
ENV LAUNCH_JBOSS_IN_BACKGROUND true

# Expose the ports we're interested in
EXPOSE 8080

# Set the default command to run on boot
# This will boot WildFly in the standalone mode and bind to all interface
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]
