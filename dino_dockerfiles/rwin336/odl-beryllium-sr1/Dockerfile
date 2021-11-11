#
# OpenDaylight Beryllium-SR1
#
# Base on hsrnetwork/odl-karaf-helium-0.2.0
#

# Pull base image
FROM ubuntu

# Author
MAINTAINER  Richard Winters <rwin336@gmail.com>

# Update the apt information
# Install OpenJDK 8 in headless mode
# Install wget
# Download distribution-karaf-0.4.1-Beryllium-SR1.tar.gz
# Install (unzip) OpenDaylight
RUN apt-get update && \
    apt-get -y install openjdk-8-jre-headless \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    echo "Download distribution-karaf-0.4.1-Beryllium-SR1.tar.gz and install" && \
    wget -q -O /opt/odl.tar.gz "http://nexus.opendaylight.org/content/groups/public/org/opendaylight/integration/distribution-karaf/0.4.1-Beryllium-SR1/distribution-karaf-0.4.1-Beryllium-SR1.tar.gz" && \
    tar -C /opt -xzf /opt/odl.tar.gz && \
    rm /opt/odl.tar.gz

# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/

# OpenDaylight Ports
# 162 - SNMP4SDN
# 179 - BGP
# 1088 - JMX access
# 1790 - BGP/PCEP
# 1830 - Netconf
# 2400 - OSGi console
# 2550 - ODL Clustering
# 2551 - ODL Clustering
# 2552 - ODL Clustering
# 4189 - PCEP
# 4342 - Lisp Flow Mapping
# 5005 - JConsole
# 5666 - ODL Internal clustering RPC
# 6633 - OpenFlow
# 6640 - OVSDB
# 6653 - OpenFlow
# 7800 - ODL Clustering
# 8000 - Java debug access
# 8080 - OpenDaylight web portal
# 8101 - KarafSSH
# 8181 - MD-SAL RESTConf and DLUX
# 8383 - Netconf
# 12001 - ODL Clustering
EXPOSE 6633 8080 8101 8181


# Define working directory.
WORKDIR /opt/distribution-karaf-0.4.1-Beryllium-SR1/bin

RUN sed -i '/^featuresBoot=/ s/$/,\
                         odl-netconf-api,\
                         odl-netconf-mapping-api,\
                         odl-netconf-util,\
                         odl-netconf-impl,\
                         odl-config-netconf-connector,\
                         odl-netconf-netty-util,\
                         odl-netconf-monitoring,\
                         odl-netconf-notifications-api,\
                         odl-netconf-notifications-impl,\
                         odl-yangtools-models,\
                         odl-yangtools-data-binding,\
                         odl-yangtools-binding,\
                         odl-yangtools-binding-generator,\
                         http,\
                         war,\
                         odl-config-persister,\
                         odl-config-startup,\
                         pax-jetty,\
                         pax-http,\
                         pax-http-whiteboard,\
                         pax-war,\
                         odl-akka-scala,\
                         odl-akka-system,\
                         odl-akka-clustering,\
                         odl-akka-leveldb,\
                         odl-akka-persistence,\
                         odl-mdsal-common,\
                         odl-mdsal-broker-local,\
                         odl-mdsal-clustering-commons,\
                         odl-mdsal-distributed-datastore,\
                         odl-mdsal-remoterpc-connector,\
                         odl-mdsal-broker,\
                         odl-config-netty,\
                         odl-aaa-authn,\
                         odl-restconf,\
                         odl-restconf-noauth/' /opt/distribution-karaf-0.4.1-Beryllium-SR1/etc/org.apache.karaf.features.cfg 

# Define default command.
CMD ["./karaf","server"]

