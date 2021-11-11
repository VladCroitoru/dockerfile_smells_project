FROM codenvy:ubuntu_jdk8
MAINTAINER Bhupal <bhupal4all@gmail.com>

RUN "wget https://services.gradle.org/distributions/gradle-3.4.1-bin.zip && sudo mkdir /opt/gradle && sudo unzip -d /opt/gradle gradle-3.4.1-bin.zip && export PATH=$PATH:/opt/gradle/gradle-3.4.1/bin"

CMD [“gradle”, “-verion”]
