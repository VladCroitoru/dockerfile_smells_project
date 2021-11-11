FROM ubuntu:14.04

RUN apt-get update -y
 
RUN apt-get install software-properties-common -y
RUN apt-add-repository ppa:webupd8team/java -y
RUN apt-get update -y
 
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections
 
RUN apt-get install -y oracle-java8-installer
RUN wget http://apache.mirror.triple-it.nl/spark/spark-1.6.1/spark-1.6.1-bin-hadoop2.6.tgz
RUN tar -xzf spark-1.6.1-bin-hadoop2.6.tgz
RUN rm spark-1.6.1-bin-hadoop2.6.tgz

RUN mv spark-1.6.1-bin-hadoop2.6 /opt/spark
 
EXPOSE 8080

RUN apt-get install -y supervisor

RUN apt-get clean
 
COPY master.conf /opt/conf/master.conf
COPY slave.conf /opt/conf/slave.conf
 
CMD ["/opt/spark/bin/spark-shell", "--master", "local[*]"]
