FROM java:7
MAINTAINER christlc

RUN apt-get update
RUN apt-get install -y wget tar sudo curl

# get drill
RUN curl -o apache-drill-1.6.0.tar.gz http://ftp.cuhk.edu.hk/pub/packages/apache.org/drill/drill-1.6.0/apache-drill-1.6.0.tar.gz

# create Drill folder
RUN sudo mkdir -p /opt/drill

# extract Drill
RUN tar -xvzf apache-drill-1.6.0.tar.gz -C /opt/drill

CMD /opt/drill/apache-drill-1.6.0/bin/drill-embedded
