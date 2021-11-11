FROM java:7
COPY src /home/root/javaHelloWorld/src
WORKDIR /home/root/javaHelloWorld
RUN mkdir bin
RUN javac -d bin src/HelloWorld.java
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]
