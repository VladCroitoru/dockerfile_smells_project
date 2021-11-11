FROM maven:3-jdk-8

ADD . $MAVEN_HOME

RUN cd $MAVEN_HOME \
 && mvn -B clean package -Djavax.xml.accessExternalSchema=all \
 && mv $MAVEN_HOME/target/$(ls $MAVEN_HOME/target | grep with-dependencies | head -1) /rulesupport.jar \
 && rm -r $MAVEN_HOME

VOLUME /src
VOLUME /target

ENTRYPOINT ["java", "-jar", "/rulesupport.jar"]
