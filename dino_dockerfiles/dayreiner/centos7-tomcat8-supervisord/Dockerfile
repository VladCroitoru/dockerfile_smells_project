FROM centos:latest
MAINTAINER dayreiner

# Tomcat and Java Vars
ENV JDK_MAJOR_VERSION=7u80 \
    JDK_VERSION=1.7.0_80 \
    TOMCAT_MAJOR_VERSION=8 \
    TOMCAT_VERSION=8.0.29 \
    JAVA_HOME=/opt/java \
    CATALINA_HOME=/opt/tomcat \
    PATH=$PATH:$JAVA_HOME/bin:${CATALINA_HOME}/bin:${CATALINA_HOME}/scripts \
    JAVA_OPTS="-Xms512m -Xmx2048m" \
    AUTHORIZED_KEYS=**None**

# Update and install latest packages and prerequisites
RUN yum -y update && yum clean all && \
    yum -y install tar openssh-server epel-release wget curl && \
    yum clean all && \
    yum -y install pwgen python-setuptools && yum clean all

ADD config/ /opt/

# Install JDK and Tomcat
RUN echo "Installing Java JDK ${JDK_VERSION}..." && \
    cd /opt && \
    wget --progress=bar -nv --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" \
    http://download.oracle.com/otn-pub/java/jdk/${JDK_MAJOR_VERSION}-b15/jdk-${JDK_MAJOR_VERSION}-linux-x64.tar.gz \
    -O /opt/jdk-${JDK_MAJOR_VERSION}-linux-x64.tar.gz && \
    echo "Checking file integrity..." && \
    sha1sum -c /opt/jdk-${JDK_MAJOR_VERSION}-linux-x64.tar.gz.sha && \
    tar xf /opt/jdk-${JDK_MAJOR_VERSION}-linux-x64.tar.gz && \
    rm jdk-${JDK_MAJOR_VERSION}-linux-x64.tar.gz && \
    mv jdk${JDK_VERSION} ${JAVA_HOME} && \
    echo "Installing Tomcat ${TOMCAT_VERSION}..." && \
    wget --progress=bar -nv http://apachemirror.ovidiudan.com/tomcat/tomcat-${TOMCAT_MAJOR_VERSION}/v${TOMCAT_VERSION}/bin/apache-tomcat-${TOMCAT_VERSION}.tar.gz \
    -O /opt/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    echo "Checking file integrity..." && \
    sha1sum -c /opt/apache-tomcat-${TOMCAT_VERSION}.tar.gz.sha && \
    tar xf /opt/apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    rm  apache-tomcat-${TOMCAT_VERSION}.tar.gz && \
    mv apache-tomcat-${TOMCAT_VERSION} ${CATALINA_HOME} && \
    chmod +x ${CATALINA_HOME}/bin/*sh

# SSH, Tomcat and supervisord setup
ADD scripts/ ${CATALINA_HOME}/scripts/
RUN chmod +x ${CATALINA_HOME}/scripts/*.sh && \
    groupadd -r tomcat && \
    useradd -g tomcat -d ${CATALINA_HOME} -s /sbin/nologin  -c "Tomcat user" tomcat && \
    chown -R tomcat: ${CATALINA_HOME} && \
    ${CATALINA_HOME}/scripts/create_admin.sh && \
    echo "Setup SSH..." && \
    rm -f /etc/ssh/ssh_host_ecdsa_key /etc/ssh/ssh_host_rsa_key && \
    ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_ecdsa_key && \
    ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key && \
    sed -i "s/#UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config && \
    echo "Setup supervisord..." && \
    mv /opt/supervisord.conf /etc/supervisord.conf && \
    chmod 666 /etc/supervisord.conf && \
    easy_install supervisor && \
    ${CATALINA_HOME}/scripts/ssh-setup.sh

# Expose and Start Services
WORKDIR ${CATALINA_HOME}
EXPOSE 22 8080 8009
CMD ["/usr/bin/supervisord"]
