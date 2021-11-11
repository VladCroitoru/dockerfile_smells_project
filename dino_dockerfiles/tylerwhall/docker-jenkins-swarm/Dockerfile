FROM fedora:20

RUN yum -y install java-1.8.0-openjdk curl jq redhat-lsb-core

RUN adduser -d /var/lib/jenkins jenkins

ADD resources /var/lib/jenkins
# Add the swarm client
RUN curl http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-client/1.15/swarm-client-1.15-jar-with-dependencies.jar > /var/lib/jenkins/swarm-client.jar

ENTRYPOINT ["/bin/su", "jenkins", "-c", "/var/lib/jenkins/jenkins_start.sh"]
