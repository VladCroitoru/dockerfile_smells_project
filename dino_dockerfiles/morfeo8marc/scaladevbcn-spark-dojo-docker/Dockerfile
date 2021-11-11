# This container is specially created for the scala barcelona's spark codign dojo  http://www.meetup.com/Scala-Developers-Barcelona/events/219559060/
# Inspired in:
#
# https://github.com/dockerfile/java
# https://github.com/dockerfile/java/tree/master/oracle-java8
# https://github.com/jamesdbloom/docker_java8_maven

FROM dockerfile/java:oracle-java8

MAINTAINER Marc Navarro https://github.com/morfeo8marc

# update packages and install maven
RUN  \
  export DEBIAN_FRONTEND=noninteractive && \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y vim wget curl git maven

# attach volumes
VOLUME /volume/git

# create working directory
RUN mkdir -p /dojo/git


# Now the install instructions for spark provided by the meetup
# Download and build spark
RUN mkdir -p /dojo/spark/tmp
RUN cd /dojo/spark/tmp
WORKDIR /dojo/spark/tmp
RUN wget https://d3kbcqa49mib13.cloudfront.net/spark-1.2.0.tgz
RUN tar xvfz spark-1.2.0.tgz
RUN mv spark-1.2.0 ../
RUN cd /dojo/spark/spark-1.2.0
RUN /dojo/spark/spark-1.2.0/make-distribution.sh --skip-java-test

# Obtain database set
RUN mkdir -p /dojo/spark/dataset
RUN cd /dojo/spark/dataset
WORKDIR /dojo/spark/dataset
RUN wget https://dumps.wikimedia.org/other/pagecounts-raw/2015/2015-01/pagecounts-20150101-000000.gz
RUN wget https://dumps.wikimedia.org/other/pagecounts-raw/2015/2015-01/pagecounts-20150101-010000.gz
RUN wget https://dumps.wikimedia.org/other/pagecounts-raw/2015/2015-01/pagecounts-20150101-020000.gz
RUN gunzip pagecount*

WORKDIR /dojo/git

# run terminal
CMD ["/bin/bash"]
