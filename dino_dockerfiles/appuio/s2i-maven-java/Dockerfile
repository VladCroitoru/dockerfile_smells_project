FROM openshift/base-centos7

MAINTAINER Tobias Brunner <tobias.brunner@vshn.ch>

ENV MAVEN_VERSION=3.5.2

# Docker Image Metadata
LABEL io.k8s.description="Platform for building (Maven) and running plain Java applications" \
      io.k8s.display-name="Java Applications" \
      io.openshift.tags="builder,java,maven" \
      io.openshift.expose-services="8080" \
      org.jboss.deployments-dir="/deployments"

# Install Java
RUN INSTALL_PKGS="java-1.8.0-openjdk java-1.8.0-openjdk-devel" && \
    yum install -y $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all -y && \
    mkdir -p /opt/s2i/destination

# Install Maven
RUN wget -q http://www-eu.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz && \
    mkdir /opt/maven && \
    tar xzf apache-maven-${MAVEN_VERSION}-bin.tar.gz -C /opt/maven && \
    rm apache-maven-${MAVEN_VERSION}-bin.tar.gz && \
    ln -s /opt/maven/apache-maven-${MAVEN_VERSION}/bin/mvn /usr/local/bin/mvn

# S2I scripts
COPY ./s2i/bin/ /usr/libexec/s2i

RUN chown -R 1001:1001 /opt/app-root
USER 1001

EXPOSE 8080

CMD ["/usr/libexec/s2i/usage"]
