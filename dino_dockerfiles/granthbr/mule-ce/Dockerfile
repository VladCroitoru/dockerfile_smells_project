# Temporarilty lifted from V Romero at Mulesoft. 
# changes coming to Dockerfile

FROM java:7
MAINTAINER brandon grantham <brandon.grantham@gmail.com>

RUN cd ~ && wget https://repository-master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-standalone/3.8.0/mule-standalone-3.8.0.tar.gz && echo "d9279b3f0373587715613341a16483f3 mule-standalone-3.8.0.tar.gz" | md5sum -c \
	&& cd /opt && tar xvzf ~/mule-standalone-3.8.0.tar.gz && rm ~/mule-standalone-3.8.0.tar.gz && ln -s /opt/mule-standalone-3.8.0 /opt/mule

# Define environment variables.
ENV MULE_HOME /opt/mule

VOLUME ["/opt/mule/logs", "/opt/mule/conf", "/opt/mule/apps", "/opt/mule/domains"]

# Define working directory.
WORKDIR /opt/mule

CMD [ "/opt/mule/bin/mule" ]

# Default http port
EXPOSE 8081

CMD [ "/opt/mule/bin/mule" ]
