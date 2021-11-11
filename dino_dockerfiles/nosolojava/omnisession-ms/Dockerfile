FROM maven

MAINTAINER nosolojava


WORKDIR $HOME/

# execute common ms until is in maven repo
RUN git clone https://github.com/nosolojava/common-ms
WORKDIR $HOME/common-ms/
RUN mvn clean install

# add maven files
WORKDIR $HOME/omnisession-ms/
ADD pom.xml $HOME/omnisession-ms/
ADD src/ $HOME/omnisession-ms/src/

# build MS 
WORKDIR $HOME/omnisession-ms/
RUN mvn clean install spring-boot:repackage

EXPOSE 8080
WORKDIR $HOME/omnisession-ms/target
CMD java -jar $HOME/target/omnisession-ms.jar