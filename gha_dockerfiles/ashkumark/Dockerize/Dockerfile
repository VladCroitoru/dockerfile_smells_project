


#FROM maven:3.8.2-openjdk-8

FROM jenkins/jenkins:lts
LABEL maintainer="ash"

#WORKDIR /home/docker
#COPY src /home/docker/src
#COPY pom.xml /home/docker

WORKDIR /home/docker-jenkins-test
COPY src /home/docker-jenkins-test
COPY pom.xml /home/docker-jenkins-test

ENV JAVA_OPTS="-Xmx8192m"
ENV JENKINS_OPTS="--logfile=/var/log/jenkins/jenkins.log"

USER root

RUN apt-get update && \
    apt-get install -y sudo maven gnupg wget curl unzip --no-install-recommends && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
    apt-get update -y && \
    apt-get install -y google-chrome-stable && \
    CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
    DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && \
    wget -q --continue -P /chromedriver "http://chromedriver.storage.googleapis.com/$DRIVERVER/chromedriver_linux64.zip" && \
    unzip /chromedriver/chromedriver* -d /chromedriver
    
RUN chown -R jenkins:jenkins /chromedriver

RUN mkdir /var/log/jenkins
RUN chown -R  jenkins:jenkins /var/log/jenkins

# entrypoint is used to update docker gid and revert back to jenkins user
#COPY entrypoint.sh /home/docker-jenkins-test/entrypoint.sh
#RUN chmod +x /home/docker-jenkins-test/entrypoint.sh
#ENTRYPOINT ["/home/docker-jenkins-test/entrypoint.sh"]

USER jenkins
  
# Expose ports
EXPOSE 5901