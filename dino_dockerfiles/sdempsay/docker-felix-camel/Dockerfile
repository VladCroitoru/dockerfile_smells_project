FROM pavlovmedia/pavlov-felix-container
MAINTAINER Shawn Dempsay <shawn@dempsay.org>

ENV DEBIAN_FRONTEND noninteractive

# Camel
ENV camel_version 2.16.1
ENV camel_base http://repo1.maven.org/maven2/org/apache/camel

# Next up is camel
ADD ${camel_base}/camel-core/${camel_version}/camel-core-${camel_version}.jar /opt/felix/current/bundle/
ADD ${camel_base}/camel-core-osgi/${camel_version}/camel-core-osgi-${camel_version}.jar /opt/felix/current/bundle/
ADD ${camel_base}/camel-scr/${camel_version}/camel-scr-${camel_version}.jar /opt/felix/current/bundle/
