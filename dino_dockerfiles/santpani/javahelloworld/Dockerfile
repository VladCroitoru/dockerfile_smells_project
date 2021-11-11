FROM java:7
MAINTAINER DockerTraining <santpani@cisco.com>

COPY src /home/root/javahelloworld/src
WORKDIR /home/root/javahelloworld
RUN mkdir bin
RUN javac -d bin src/HelloWorld.java
#ENTRYPOINT ["java","-cp","bin","HelloWorld"]
RUN mkdir -p /data/myvol
RUN echo "hi this is a test file" > /data/myvol/test

