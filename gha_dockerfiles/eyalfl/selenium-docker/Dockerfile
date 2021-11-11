FROM openjdk:15-ea-31-jdk-alpine

RUN apk add curl jq
#Workspace
WORKDIR /usr/share/udemy

# ADD .jar under target from host
# into this image
ADD target/selenium-docker.jar          selenium-docker.jar
ADD target/selenium-docker-tests.jar    selenium-docker-tests.jar
ADD target/libs                         libs

# ADD suite files
ADD book-flight-module-testng.xml       book-flight-module-testng.xml
ADD search-testng.xml                   search-testng.xml
ADD healthcheck.sh                      healthcheck.sh

# convert file from Windows to Unix format
RUN dos2unix healthcheck.sh

# BROWSER
# HUB_HOST
# MODULE
#ENTRYPOINT java -cp selenium-docker.jar:selenium-docker-tests.jar:libs/* -DBROWSER=$BROWSER -DHUB_HOST=$HUB_HOST org.testng.TestNG $MODULE

ENTRYPOINT sh ./healthcheck.sh
