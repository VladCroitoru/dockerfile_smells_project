FROM ubuntu:16.04
ADD http://85-207-0-21.static.bluetone.cz/java/1.6.0_45/jdk-6u45-linux-x64.bin ./jdk-6-x64.bin
RUN chmod +x jdk-6-x64.bin
RUN ./jdk-6-x64.bin
RUN rm jdk-6-x64.bin
ADD http://archive.apache.org/dist/maven/binaries/apache-maven-2.2.1-bin.tar.gz .
RUN tar -xzf apache-maven-2.2.1-bin.tar.gz
ENV PATH $PATH:/jdk1.6.0_45/bin:/apache-maven-2.2.1/bin/
ENV JAVA_HOME /jdk1.6.0_45
ENV M2_HOME /apache-maven-2.2.1/
ENV M2_REPO /root/.m2
ENTRYPOINT ["mvn"]
WORKDIR /root/project
