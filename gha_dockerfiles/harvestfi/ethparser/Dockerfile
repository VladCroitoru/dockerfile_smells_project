FROM openjdk:11
COPY ./dist /dist
WORKDIR /dist
CMD java -XX:+UseContainerSupport ${JAVA_ARGS} -jar ethparser.jar
