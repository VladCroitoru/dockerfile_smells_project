FROM alpine
LABEL maintener="pokido99@gmail.com"

# Proxy settings if necessary
# ENV http_proxy=http://proxy:8080
# ENV https_proxy=http://proxy:8080
# ENV no_proxy="127.0.0.1,localhost,.mydomain.com"

# Upgrade all packages 
RUN apk --no-cache upgrade

# Install Java
RUN apk --no-cache add openjdk8-jre

# Install tools and dependencies
RUN apk --no-cache add curl bash fontconfig ttf-dejavu

# Install Jenkins
ENV JENKINS_USER jenkins
ENV JENKINS_VERSION 2.70
ENV JENKINS_HOME /opt/jenkins

# With proxy
# ENV JAVA_OPTS -Djava.awt.headless=true -Dhttp.proxyHost=proxyva.mydomain.com -Dhttp.proxyPort=8080 -Dhttps.proxyHost=proxyva.mydomain.com -Dhttps.proxyPort=8080

ENV JAVA_OPTS -Djava.awt.headless=true
RUN mkdir /opt && adduser -Dh $JENKINS_HOME $JENKINS_USER && cd $JENKINS_HOME && curl -sL -O http://mirrors.jenkins.io/war/$JENKINS_VERSION/jenkins.war

USER $JENKINS_USER
EXPOSE 8080

CMD /usr/bin/java $JAVA_OPTS -jar $JENKINS_HOME/jenkins.war
