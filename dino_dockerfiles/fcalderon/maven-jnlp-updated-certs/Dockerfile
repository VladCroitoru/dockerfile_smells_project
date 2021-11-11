FROM microsoft/java-on-azure-jenkins-slave

ADD . /home/jenkins
#
##ENTRYP ["mvn", "clean"install"]
RUN cd /usr/local/share/ca-certificates \
&& update-ca-certificates \
&& ln -sf /etc/ssl/certs/java/cacerts $JAVA_HOME/jre/lib/security/cacerts
