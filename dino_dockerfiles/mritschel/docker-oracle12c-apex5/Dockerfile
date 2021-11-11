##########################################################################
#  Author   M. Ritschel 
#           Trivadis GmbH Hamburg
#  Created: 28.06.2016 
#  Base-information 
#  ------------------------
# This Image based on https://hub.docker.com/r/mritschel/oraclebase/
#  
##########################################################################
FROM mritschel/oraclebase

MAINTAINER Martin.Ritschel@Trivadis.com

LABEL Basic oracle 12c.R1 with java and perl

# Environment
ENV DBCA_TOTAL_MEMORY=1024
ENV ORACLE_BASE=/u01/app/oracle
ENV ORACLE_HOME=$ORACLE_BASE/product/12.1.0.2/dbhome_1
ENV ORACLE_DATA=/u00/app/oracle/oradata 
ENV ORACLE_HOME_LISTNER=$ORACLE_HOME
ENV SERVICE_NAME=xe.oracle.docker
ENV PATH=$ORACLE_HOME/bin:$PATH
ENV NLS_DATE_FORMAT=DD.MM.YYYY\ HH24:MI:SS 
ENV ORACLE_SID=xe
ENV APEX_PASS=Manager_12C
ENV PASS=oracle  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle
ENV INSTALL_HOME=$ORACLE_BASE/install
ENV SCRIPTS_HOME=$ORACLE_BASE/scripts

# Fix sh
#RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Installing the required software 
USER root
RUN yum -y install unzip wget zip gcc ksh sudo && \
    yum clean all
    
# Copy the installation files
ADD software $INSTALL_HOME
ADD scripts  $SCRIPTS_HOME
RUN unzip $INSTALL_HOME/apex_5.0.3_1.zip -d $INSTALL_HOME >/dev/null 2>&1
RUN rm -f $INSTALL_HOME/apex_5.0.3_1.zip 
RUN unzip $INSTALL_HOME/apex_5.0.3_2.zip -d $INSTALL_HOME >/dev/null 2>&1
RUN rm -f $INSTALL_HOME/apex_5.0.3_2.zip 
RUN chmod -R 777 $INSTALL_HOME/*
RUN chown -R oracle:dba $INSTALL_HOME/* 
RUN chmod -R 777 $SCRIPTS_HOME/*
RUN chown -R oracle:dba $SCRIPTS_HOME/* 

# start the installation scripts
USER oracle
RUN $SCRIPTS_HOME/install.sh


# Ports 
EXPOSE 1521 
EXPOSE 8080

# Startup script to start the database in container
ENTRYPOINT ["/u01/app/oracle/scripts/entrypoint.sh"]

# Define default command.
#CMD ["bash"]
