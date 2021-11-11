FROM debian:wheezy

MAINTAINER dev@huttopia.com

ENV DEBIAN_FRONTEND noninteractive

# Install java
RUN apt-get update && apt-get install -y \
    openjdk-7-jre

# Install firefox
RUN apt-get install -y \
    xvfb \
    iceweasel

# Install selenium
ADD http://selenium-release.storage.googleapis.com/2.44/selenium-server-standalone-2.44.0.jar /opt/selenium.jar

ENV DISPLAY :99

EXPOSE 4444

CMD $(Xvfb :99 -ac -screen 0 1280x1024x24 &); java -jar /opt/selenium.jar -browser iceweasel
