# s2i-java
FROM openshift/base-centos7
MAINTAINER Maurizio Pillitu <maoo@apache.org>
# HOME in base image is /opt/app-root/src

# Install build tools on top of base image
# Java jdk 8, Maven 3.3, Gradle 2.6
RUN INSTALL_PKGS="net-tools openssl tar unzip bc which lsof java-11-openjdk java-11-openjdk-devel" && \
    yum install -y --enablerepo=centosplus $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    yum clean all -y && \
    mkdir -p /opt/openshift && \
    mkdir -p /opt/app-root/source && chmod -R a+rwX /opt/app-root/source && \
    mkdir -p /opt/s2i/destination && chmod -R a+rwX /opt/s2i/destination && \
    mkdir -p /opt/app-root/src && chmod -R a+rwX /opt/app-root/src

LABEL io.k8s.description="Platform for packing Java (executable) applications" \
      io.k8s.display-name="Java Binaries S2I builder 1.0" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,java,microservices,appassembler"

LABEL io.openshift.s2i.scripts-url=image:///usr/local/sti
COPY ./sti/bin/ /usr/local/sti

RUN chown -R 1001:1001 /opt/openshift

# This default user is created in the openshift/base-centos7 image
USER 1001

# Set the default port for applications built using this image
EXPOSE 8080

# Set the default CMD for the image
# CMD ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/opt/openshift/app.jar"]
CMD ["usage"]
