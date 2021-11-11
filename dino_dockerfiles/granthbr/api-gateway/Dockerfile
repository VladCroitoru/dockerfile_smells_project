# Dockerizing MuleSoft Api-Gateway
# Version:  0.1
# Based on:  java (Trusted Java from http://java.com)

FROM                   java
MAINTAINER             Brandon Grantham <brandon.grantham@gmail.com>

WORKDIR /opt/

# This line can reference either a web url (ADD), network share or local file (COPY)
RUN curl https://s3.amazonaws.com/static-anypoint-mulesoft-com/api-gateway-distribution-standalone-2.2.0.zip > api-gateway.zip &&  \
unzip api-gateway.zip -d /opt &&  mv /opt/$(ls -1t|tail -1) /opt/api-gateway && rm api-gateway.zip

# Mule remote debugger
EXPOSE  5000

EXPOSE 8083

EXPOSE 8082


# Mule JMX port (must match Mule config file)
EXPOSE  1098

# Mule MMC agent port
EXPOSE  7777

# Environment and execution:

ENV             MULE_BASE /opt/api-gateway
ENV             mule_base /opt/api-gateway
WORKDIR         /opt/api-gateway
CMD             ./bin/gateway