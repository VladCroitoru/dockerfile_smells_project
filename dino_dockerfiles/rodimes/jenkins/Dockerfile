FROM  jenkins/jenkins:lts

COPY docker/plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

ENV JENKINS_OPTS --prefix=/jenkins
