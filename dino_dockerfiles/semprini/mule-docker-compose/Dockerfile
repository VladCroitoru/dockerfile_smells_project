FROM java:openjdk-8-jdk

MAINTAINER https://github.com/Semprini

# Define environment variables.
ENV MULE_HOME /opt/mule
ENV MULE_APPS_ARCHIVE https://nexus.rancher.sphinx.co.nz/repository/files/mulehelloworldexample.zip
ENV MULE_APPS_DEST mulehelloworldexample.zip

# Get mule standalone from Mulesoft and extract
RUN cd ~ && wget https://repository-master.mulesoft.org/nexus/content/repositories/releases/org/mule/distributions/mule-standalone/3.8.0/mule-standalone-3.8.0.tar.gz && echo "d9279b3f0373587715613341a16483f3 mule-standalone-3.8.0.tar.gz" | md5sum -c
RUN cd /opt && tar xvzf ~/mule-standalone-3.8.0.tar.gz && rm ~/mule-standalone-3.8.0.tar.gz && ln -s /opt/mule-standalone-3.8.0 /opt/mule

# nexus containing apps artifact
RUN wget --no-check-certificate --output-document $MULE_APPS_DEST $MULE_APPS_ARCHIVE
RUN unzip -t $MULE_APPS_DEST
#RUN unzip ${MULE_APPS_DEST}
RUN cp $MULE_APPS_DEST /opt/mule/apps/

# Define mount points.
VOLUME ["/opt/mule/logs", "/opt/mule/conf", "/opt/mule/apps", "/opt/mule/domains"]

# Define working directory.
WORKDIR /opt/mule

CMD [ "/opt/mule/bin/mule" ]
