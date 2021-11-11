FROM java:7

#COPY HelloWorld.java /
COPY src /home/root/javahelloworld/src

#RUN javac HelloWorld.java
WORKDIR /home/root/javahelloworld
RUN mkdir bin
RUN mkdir data_dir
RUN javac -d bin src/HelloWorld.java

#ENTRYPOINT ["java", "HelloWorld"]
ENTRYPOINT ["java", "-cp", "bin", "HelloWorld"]





