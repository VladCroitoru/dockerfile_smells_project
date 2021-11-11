FROM java:8
ENV FOO bar
WORKDIR /home/root/javahelloworld
COPY src src 

RUN mkdir bin
RUN javac -d bin src/HelloWorld.java
CMD sudo apt-get install -y wwwstat 
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]
