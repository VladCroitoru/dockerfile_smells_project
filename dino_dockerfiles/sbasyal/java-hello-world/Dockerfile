FROM java:7
MAINTAINER Sabin Basyal<sabin.basyal@docker.com>

COPY src /home/root/java/src
WORKDIR /home/root/java
RUN mkdir bin
RUN javac -d bin src/HelloWorld.java

ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]

ONBUILD ADD . /home/test.txt
