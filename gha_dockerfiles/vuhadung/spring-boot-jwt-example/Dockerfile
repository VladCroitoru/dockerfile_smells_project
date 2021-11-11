FROM centos:8

RUN yum update -y && \
  yum install -y wget && \
  yum install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel && \
  yum clean all

RUN yum install -y make && yum clean all

RUN dnf group install "Development Tools" -y

RUN yum update -y && \
  yum install -y epel-release && \
  yum install -y boost boost-thread boost-devel && \
  yum clean all

ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64
# ENV PATH "$PATH:${JAVA_HOME}/bin"

ARG JAR_FILE=target/*.jar
COPY ${JAR_FILE} app.jar

#Escaping is possible by adding a \ before the variable: \$foo or \${foo}
#For example, will translate to $foo and ${foo} literals respectively
ENV APP_OPTS="--spring.datasource.url=\${CONNECTION_URL}"
ENV APP_OPTS="${APP_OPTS} --spring.datasource.username=\${CONNECTION_USERNAME}"
ENV APP_OPTS="${APP_OPTS} --spring.datasource.password=\${CONNECTION_PASSWORD}"
ENV APP_OPTS="${APP_OPTS} --file.game-dir=\${GAME_DIR}"

RUN echo ${APP_OPTS}
ENTRYPOINT java -jar /app.jar ${APP_OPTS}
