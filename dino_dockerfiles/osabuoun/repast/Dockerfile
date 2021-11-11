FROM java:openjdk-7-jdk

COPY Repast2.tar /opt
COPY execute.sh /opt

RUN mkdir /opt/repast
RUN tar -xvf  /opt/Repast2.tar -C /opt/repast
RUN chmod +x /opt/execute.sh
#CMD ["/opt/execute.sh" ]
