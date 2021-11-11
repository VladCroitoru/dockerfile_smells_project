# DOCKER-VERSION 1.0.1
FROM ubuntu:14.04
MAINTAINER bpauli

# Update the APT cache
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y

# Install and setup project dependencies
RUN apt-get install -y curl wget
RUN locale-gen en_US en_US.UTF-8

#prepare for Java download
RUN apt-get install -y python-software-properties
RUN apt-get install -y software-properties-common

#grab oracle java (auto accept licence)
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections
RUN apt-get install -y oracle-java7-installer

# Install python and python modules
RUN apt-get install -y python-psutil
RUN apt-get install -y python-requests
RUN apt-get install -y python-simplejson

# Install utility for AEM
ADD aemInstaller.py /aem/aemInstaller.py

#Copies required build media
ONBUILD ADD cq-publish-4503.jar /aem/cq-publish-4503.jar
ONBUILD ADD license.properties /aem/license.properties

# Extracts AEM
ONBUILD WORKDIR /aem
ONBUILD RUN java -XX:MaxPermSize=256m -Xmx1024M -jar cq-publish-4503.jar -unpack -r nosamplecontent
ONBUILD RUN python aemInstaller.py -i cq-publish-4503.jar -r publisher -p 4503

ONBUILD WORKDIR /aem/crx-quickstart/bin
#Replaces the port within the quickstart file with the standard publisher port
ONBUILD RUN cp quickstart quickstart.original
ONBUILD RUN cat quickstart.original | sed "s|4502|4503|g" > quickstart

EXPOSE 4503
ENTRYPOINT ["/aem/crx-quickstart/bin/quickstart"]
