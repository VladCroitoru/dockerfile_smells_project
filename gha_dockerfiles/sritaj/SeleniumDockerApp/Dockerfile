FROM  openjdk:18-jdk-alpine3.13

RUN apk add curl jq

#WORKSPACE
WORKDIR /usr/share/udemy

#ADD .jar from Target to Host
#into this image
ADD target/selenium-docker.jar           selenium-docker.jar
ADD target/selenium-docker-tests.jar     selenium-docker-tests.jar
ADD target/libs                          libs

#ADD XML SUITE files
ADD flight-details-test.xml              flight-details-test.xml
ADD registration-confimration-test.xml   registration-confimration-test.xml
ADD user-registration-test.xml           user-registration-test.xml

#copy if any other dependencies are there like test-data files, properties files etc

#Add health check script
ADD healthcheck.sh                       healthcheck.sh

#passing multiple env variables, browser, host address, moduleds
ENTRYPOINT sh healthcheck.sh
# ENTRYPOINT java -cp selenium-docker.jar:selenium-docker-tests.jar:libs/* -DBROWSER=$BROWSER -DHUB_HOST=$HUB_HOST org.testng.TestNG $MODULE
