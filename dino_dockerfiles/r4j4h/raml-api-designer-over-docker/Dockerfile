FROM ubuntu:precise


# Install dependencies
RUN apt-get -y update
RUN apt-get install -y bridge-utils wget dnsmasq build-essential python nodejs nodejs-dev npm 


# Install Pre-reqs
RUN apt-get install -y git


# Install Node
ADD install/install-node.sh /usr/bin/install-node.sh
RUN install-node.sh


# Install RAML API Designer
ADD install/install-raml-api-designer.sh /usr/bin/install-raml-api-designer.sh
RUN install-raml-api-designer.sh


# Run Provisioning Script
ADD install/bootstrap.sh /usr/bin/bootstrap.sh
RUN bootstrap.sh


WORKDIR /usr/local/api-designer

EXPOSE 9013
EXPOSE 35730
