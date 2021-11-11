# escape=\
FROM jenkins:docker
USER root
RUN apt-get update
RUN apt-get install -y \
apt-transport-https \
ca-certificates \
curl \
git \
gnupg2 \
software-properties-common
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add -
RUN add-apt-repository \
"deb [arch=amd64] https://download.docker.com/linux/debian \
$(lsb_release -cs) \
stable"
RUN apt-get update
RUN apt-get install -y docker-ce
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"
RUN mkdir -p /var/jenkins_home/init.groovy.d && chown jenkins:jenkins /var/jenkins_home/init.groovy.d
USER jenkins
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:8080/status/ || exit 1
COPY init.groovy.d /var/jenkins_home/init.groovy.d
COPY plugins.txt /usr/share/jenkins/ref/
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt
