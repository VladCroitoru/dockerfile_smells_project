# Apache Drill v1.6.0 - distributed mode
#
# VERSION 0.1 - not for production, use at own risk
# General instructions: https://drill.apache.org/docs/install-drill-introduction/
#


#
# Using Ubuntu as the base image
#
FROM java:7

MAINTAINER skydjol@gmail.com

#
# Prerequisite: Install Java, tar and create Drill folders
# http://doc.mapr.com/display/MapR/Preparing+Each+Node#PreparingEachNode-java
#
RUN apt-get update && apt-get install -y tar && \
    mkdir -p /drill-scripts && \
    mkdir -p /opt/drill
#
# Download and Install Apache Drill
# https://drill.apache.org/docs/installing-drill-on-linux-and-mac-os-x/
#
RUN curl -o apache-drill-1.6.0.tar.gz http://www.eu.apache.org/dist/drill/drill-1.6.0/apache-drill-1.6.0.tar.gz && \
    tar zxpf apache-drill-1.6.0.tar.gz -C /opt/drill && rm -fr apache-drill-1.6.0.tar.gz

#
# Start Apache Drill in embedded mode
# https://drill.apache.org/docs/starting-drill-on-linux-and-mac-os-x/
#
ADD bootstrap.sh /drill-scripts/bootstrap.sh
RUN chown root:root /drill-scripts/bootstrap.sh && \
    chmod 700 /drill-scripts/bootstrap.sh
ENV BOOTSTRAP /drill-scripts/bootstrap.sh

#
# Expose the Apache Drill Web UI
# https://drill.apache.org/docs/storage-plugin-registration/
#
EXPOSE 8047 31010 31011 31012 46655/udp
CMD /drill-scripts/bootstrap.sh && tail -f /opt/drill/apache-drill-1.6.0/log/drillbit.out
