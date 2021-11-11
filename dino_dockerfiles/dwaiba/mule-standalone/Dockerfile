FROM java:openjdk-8-jdk

MAINTAINER dbanerj@gmail.com

RUN cd ~ && wget https://repository-master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-standalone/3.8.1/mule-standalone-3.8.1.tar.gz && echo "db079c0fc01c534d443277cfe96ab252 mule-standalone-3.8.1.tar.gz" | md5sum -c

RUN cd /opt && tar xvzf ~/mule-standalone-3.8.1.tar.gz && rm -rf ~/mule-standalone-3.8.1.tar.gz && ln -s /opt/mule-standalone-3.8.1 /opt/mule

# Define environment variables.
ENV MULE_HOME /opt/mule

# Define mount points.
VOLUME ["/opt/mule/logs", "/opt/mule/conf", "/opt/mule/apps", "/opt/mule/domains"]
# Define working directory.
WORKDIR /opt/mule
RUN cd /opt/mule/bin && wget https://mule-agent.s3.amazonaws.com/1.7.1/agent-setup-1.7.1.zip && unzip agent-setup-1.7.1.zip && rm -rf agent-setup-1.7.1.zip  && mkdir ../plugins && ./amc_setup -I 

# Default http port
EXPOSE 8081
EXPOSE 7777

CMD ["/opt/mule/bin/./mule", "start"]
#CMD [ "/opt/mule/bin/mule" ]
