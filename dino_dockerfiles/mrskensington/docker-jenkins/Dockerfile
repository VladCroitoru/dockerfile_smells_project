FROM debian:jessie
MAINTAINER Mike Ditum "docker@mikeditum.co.uk"

RUN apt-get update && \
    apt-get --no-install-recommends install -q -y openjdk-7-jre-headless git && \
    rm -rf /var/lib/apt/lists/*
ADD http://mirrors.jenkins-ci.org/war/latest/jenkins.war /opt/jenkins.war
RUN chmod 644 /opt/jenkins.war
ENV JENKINS_HOME /jenkins

ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]
EXPOSE 8080
CMD [""]
