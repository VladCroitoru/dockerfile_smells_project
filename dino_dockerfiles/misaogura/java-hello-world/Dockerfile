FROM java:8
MAINTAINER Misa Ogura <misa.ogura01@gmail.com>

COPY src /home/root/javahelloworld/src
WORKDIR /home/root/javahelloworld

RUN mkdir bin && \
    javac -d bin src/HelloWorld.java

RUN apt-get -y update && \
    apt-get install -y vim

ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]
