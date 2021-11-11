FROM java:openjdk-7-jre

MAINTAINER Oliver Lade <piemaster21@gmail.com>
# See https://github.com/NetLogo/NetLogo/wiki/Controlling-API

ENV NETLOGO_HOME /opt/netlogo

# Download and extract NetLogo to /opt/netlogo.
RUN wget https://ccl.northwestern.edu/netlogo/5.1.0/netlogo-5.1.0.tar.gz && \
    tar xzf netlogo-5.1.0.tar.gz && \
    rm netlogo-5.1.0.tar.gz && \
    mv netlogo-5.1.0 $NETLOGO_HOME 

