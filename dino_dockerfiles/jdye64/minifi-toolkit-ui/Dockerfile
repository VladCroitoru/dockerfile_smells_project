FROM java:8u91-jdk
MAINTAINER Jeremy Dyer <jdye64@gmail.com>

EXPOSE 9050

ADD releases/minifi-toolkit-ui-0.1.0-SNAPSHOT.jar /
ADD application.yml /
CMD java -jar /minifi-toolkit-ui-0.1.0-SNAPSHOT.jar server /application.yml