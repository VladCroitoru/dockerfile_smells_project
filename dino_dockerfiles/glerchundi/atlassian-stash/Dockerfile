FROM quay.io/justcontainers/base:v0.8.1
MAINTAINER Gorka Lerchundi Osa <glertxundi@gmail.com>

##
## INSTALL
##

# accept terms and add custom oracle repo
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
    add-apt-repository -y ppa:webupd8team/java

# install oracle java 8 & git
RUN apt-get-min update                             && \
    apt-get-install-min oracle-java8-installer git

# define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# create stash user
RUN useradd -r -s /bin/false stash

# atlassian stash
ADD https://www.atlassian.com/software/stash/downloads/binary/atlassian-stash-3.10.0.tar.gz /tmp/atlassian-stash.tar.gz
RUN mkdir -p /opt/stash && \
    mkdir -p /opt/stash/conf/Catalina && \
    tar xvfz /tmp/atlassian-stash.tar.gz -C /opt/stash --strip 1 --owner stash --group stash

# mysql connector
ADD http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-5.1.35.tar.gz /tmp/mysql-connector.tar.gz
RUN tar xvfz /tmp/mysql-connector.tar.gz -C /opt/stash/lib --strip 1 --wildcards --no-anchored 'mysql-connector-java-5.1.35-bin.jar'

# directory in which stash will save persistent data
ENV STASH_HOME /var/lib/stash

# confd
ADD https://github.com/glerchundi/confd/releases/download/v0.10.0-beta1/confd-0.10.0-beta1-linux-amd64 /usr/bin/confd
RUN chmod 0755 /usr/bin/confd

##
## ROOTFS
##

# root filesystem
COPY rootfs /

# data & log volumes
VOLUME [ "/var/lib/stash" ]

# ports (http & ssh)
EXPOSE 7990
EXPOSE 7999

##
## CLEANUP
##

RUN apt-cleanup
