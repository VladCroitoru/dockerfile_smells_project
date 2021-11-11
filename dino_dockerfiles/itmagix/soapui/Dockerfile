FROM centos:7
MAINTAINER Maikel Dolle <maikel@itmagix.nl>

# Version
ENV SOAPUI_VERSION 5.4.0

COPY src/entry_point.sh /opt/bin/entry_point.sh
COPY src/server.py /opt/bin/server.py
COPY src/server_index.html /opt/bin/server_index.html

RUN chmod +x /opt/bin/entry_point.sh
RUN chmod +x /opt/bin/server.py

# Update container and install needed packages
RUN yum -y update && yum -y install curl java-1.8.0-openjdk

# Set timezone
RUN rm -rf /etc/localtime
RUN ln -s /usr/share/zoneinfo/Europe/Amsterdam /etc/localtime

# Download and unarchive SoapUI
RUN mkdir -p /opt && \
    curl https://s3.amazonaws.com/downloads.eviware/soapuios/${SOAPUI_VERSION}/SoapUI-${SOAPUI_VERSION}-linux-bin.tar.gz \
    | gunzip -c - | tar -xf - -C /opt && \
    ln -s /opt/SoapUI-${SOAPUI_VERSION} /opt/SoapUI

# Setting up some DB drivers
COPY src/ojdbc6.jar /opt/SoapUI/bin/ext/ojdbc6.jar
COPY src/h2-1.4.197.jar /opt/SoapUI/bin/ext/h2-1.4.197.jar

# Set working directory
WORKDIR /opt/bin

# Set environment
ENV PATH ${PATH}:/opt/SoapUI/bin

EXPOSE 3000
CMD ["/opt/bin/entry_point.sh"]
