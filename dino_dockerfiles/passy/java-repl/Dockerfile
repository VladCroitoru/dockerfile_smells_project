#
# Java JDK 8 REPL
#
# https://github.com/passy/java-repl
#

# Pull base image.
FROM java:8

MAINTAINER Pascal Hartig <phartig@rdrei.net>

# Define working directory.
WORKDIR /data

ADD ./javarepl.jar /data/javarepl.jar

# Define default command.
CMD ["java", "-jar", "/data/javarepl.jar"]
