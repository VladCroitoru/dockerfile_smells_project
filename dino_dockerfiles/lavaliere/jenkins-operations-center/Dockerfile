# Docker image for Jenkins Operations Center

FROM apemberton/jenkins-base
MAINTAINER Andy Pemberton <apemberton@cloudbees.com>

# Download jenkins-oc.war
USER jenkins
WORKDIR /usr/lib/jenkins
RUN curl -L -O -w "Downloaded: %{url_effective}\\n" "http://jenkins-updates.cloudbees.com/download/oc/*latest*/jenkins-oc.war"

EXPOSE 8080 22
ENV JENKINS_HOME /var/lib/jenkins

ENTRYPOINT ["java", "-jar", "jenkins-oc.war", "--httpPort=8080"]
CMD ["--prefix=/operations-center"]

# CMD ["java", "-jar", "jenkins-oc.war", "--httpPort=8080", "--prefix=/operations-center"]