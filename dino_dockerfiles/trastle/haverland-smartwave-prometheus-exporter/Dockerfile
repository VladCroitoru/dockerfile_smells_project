FROM maven:3-jdk-8 as mvnbuild
RUN mkdir -p /opt/workspace
WORKDIR /opt/workspace
COPY pom.xml .
RUN mvn -B -s /usr/share/maven/ref/settings-docker.xml dependency:resolve-plugins dependency:resolve clean package
COPY . .
RUN mvn -B -s /usr/share/maven/ref/settings-docker.xml clean package

FROM openjdk:8-jre-alpine
RUN  mkdir -p /opt/heater-tool
COPY --from=mvnbuild /opt/workspace/target/HeaterTool*.jar /opt/heater-tool
COPY config.yml /opt/heater-tool
RUN  cd /opt/heater-tool && ln -s HeaterTool*.jar HeaterTool.jar
WORKDIR /opt/heater-tool
EXPOSE 22200
CMD ["java","-jar", "HeaterTool.jar","server", "config.yml"]
