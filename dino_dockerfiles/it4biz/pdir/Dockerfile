# FROM wmarinho/ubuntu:oracle-jdk-7
# Mixed with the last two pull request from https://github.com/wmarinho/pdiR

# Docker Library 
FROM java:7

MAINTAINER Caio Moreno de Souza caiomsouza@gmail.com

# Init ENV
ENV PDI_TAG 5.3.0.0-213
ENV R_VERSION 0.0.4

# Integrating with REDIS
ENV RREDIS 1.6.9
# http://cran.rstudio.com/src/contrib/rredis_1.6.9.tar.gz

ENV PENTAHO_HOME /opt/pentaho

# Apply JAVA_HOME
RUN . /etc/environment
ENV PENTAHO_JAVA_HOME /usr/lib/jvm/java-7-oracle

RUN apt-get update \
    && apt-get install wget unzip git -y && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# Download Pentaho Data Integration (PDI) (pdi-ce-5.3.0.0-213.zip)
#RUN /usr/bin/wget -nv  http://ci.pentaho.com/view/Data%20Integration/job/kettle-5.1/lastSuccessfulBuild/artifact/assembly/dist/pdi-ce-${PDI_TAG}.zip -O /tmp/pdi-ce-${PDI_TAG}.zip 
RUN /usr/bin/wget -nv http://downloads.sourceforge.net/project/pentaho/Data%20Integration/5.3/pdi-ce-${PDI_TAG}.zip -O /tmp/pdi-ce-${PDI_TAG}.zip

RUN  /usr/bin/unzip -q /tmp/pdi-ce-${PDI_TAG}.zip -d  $PENTAHO_HOME &&\
     rm /tmp/pdi-ce-${PDI_TAG}.zip

# COPY run.sh /opt/pentaho/data-integration/
# COPY slave_dyn.xml /opt/pentaho/data-integration/

WORKDIR /opt/pentaho/data-integration

RUN apt-get update -y

RUN apt-get install r-base -y

# RUN apt-get install unzip

RUN wget -nv http://dekarlab.de/download/RScriptPlugin-${R_VERSION}.zip -O /tmp/RScriptPlugin-${R_VERSION}.zip
 
RUN unzip -q /tmp/RScriptPlugin-${R_VERSION}.zip -d /opt/ &&\
    mv /opt/RScript* ${PENTAHO_HOME}/data-integration/plugins/steps/

ENV PENTAHO_JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64

# REDIS
RUN wget -nv http://cran.rstudio.com/src/contrib/rredis_1.6.9.tar.gz -O /tmp/rredis_1.6.9.tar.gz &&\
    R CMD javareconf JAVA_HOME=${PENTAHO_JAVA_HOME} &&\
    R CMD INSTALL -l /usr/lib/R/library /tmp/rredis_1.6.9.tar.gz 

# rJava
RUN wget -nv http://cran.r-project.org/src/contrib/rJava_0.9-6.tar.gz -O /tmp/rJava_0.9-6.tar.gz &&\
    R CMD javareconf JAVA_HOME=${PENTAHO_JAVA_HOME} &&\
    R CMD INSTALL -l /usr/lib/R/library /tmp/rJava_0.9-6.tar.gz 

RUN cp /usr/lib/R/library/rJava/jri/libjri.so   ${PENTAHO_HOME}/data-integration/libswt/linux/x86_64/libjri.so

ENV R_HOME=/usr/lib/R
ENV R_LIBS_USER=/usr/lib/R/library
ENV PATH=.:$PATH:$R_HOME/bin

RUN sed -i 's/\.\.\/libswt/libswt/g' ${PENTAHO_HOME}/data-integration/spoon.sh

# Testing PDI with R step
# docker build -t pentaho/pdir .
# docker run --rm -it pentaho/pdir /opt/pentaho/test/test.sh
# COPY test /opt/pentaho/test

# EXPOSE 8181

#CMD ["./run.sh"]


