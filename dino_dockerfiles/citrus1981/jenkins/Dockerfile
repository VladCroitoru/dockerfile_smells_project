FROM citrus1981/base

RUN curl -L -C - -b "oraclelicense=accept-securebackup-cookie" -O http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.rpm && \
yum install -y ./*.rpm && \
rm *.rpm

EXPOSE 8080
EXPOSE 8009

#RUN useradd -d /home/jenkins -m -s /bin/bash jenkins
ENV JENKINS_HOME /jenkins
#RUN usermod -m -d "$JENKINS_HOME" jenkins && chown -R jenkins "$JENKINS_HOME"
VOLUME /jenkins

RUN curl -L -O http://mirrors.jenkins-ci.org/war/latest/jenkins.war
#USER jenkins

CMD ["java", "-jar", "/jenkins.war", "--httpPort=8080", "--ajp13Port=8009"]
