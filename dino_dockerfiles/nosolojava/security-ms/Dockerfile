FROM maven

MAINTAINER snorrito

# execute common ms until is in maven repo
RUN echo "building common-ms, home: "$HOME && cd $HOME && git clone https://github.com/nosolojava/common-ms && cd common-ms && mvn clean install

RUN echo "Evitando cache 456, home: "$HOME && cd $HOME && git clone https://github.com/nosolojava/security-ms.git && cd security-ms && mvn clean package spring-boot:repackage

EXPOSE 8080

CMD java -jar $HOME/security-ms/target/security-ms.jar