FROM java:7
MAINTAINER Docker Practice rami.alashi@gmail.com
COPY src /home/docker/javahelloworld/src
WORKDIR /home/docker/javahelloworld
RUN mkdir bin
RUN javac -d bin src/HelloWorld.java
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]

