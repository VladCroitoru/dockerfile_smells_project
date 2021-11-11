FROM centos:centos6
RUN yum update -y && yum install -y createrepo java-1.8.0-openjdk-headless tar
RUN curl -k -o nexus.tgz https://sonatype-download.global.ssl.fastly.net/nexus/oss/nexus-2.11.4-01-bundle.tar.gz && tar xvfz nexus.tgz -C /opt && rm nexus.tgz
# Allow nexus to run as any UID for Openshift
RUN chmod -R 777 /opt/sonatype-work/nexus /opt/nexus-2.11.4-01/logs /opt/nexus-2.11.4-01/tmp /opt/nexus-2.11.4-01/bin/jsw/linux-x86-64
COPY nexus.sh /opt/nexus-2.11.4-01/nexus.sh
EXPOSE 8081
VOLUME /opt/sonatype-work/nexus
CMD /opt/nexus-2.11.4-01/nexus.sh
