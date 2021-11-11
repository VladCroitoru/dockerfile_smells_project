FROM centos:7.6.1810
# Install useful packages
RUN yum -y update && \
  yum -y install sudo openssh-server openssh-clients openssl-devel which tar m4

WORKDIR /opt

# Install OpenJDK
RUN yum -y install java-1.8.0-openjdk-devel

# Download filebeat 5.5.2
RUN curl https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.5.2-linux-x86_64.tar.gz -o /tmp/filebeat.tar.gz

# Unzip and install filebeat
RUN tar zxf /tmp/filebeat.tar.gz -C /opt && mv /opt/filebeat-5.5.2-linux-x86_64 /opt/filebeat && rm -rf /tmp/filebeat.tar.gz

