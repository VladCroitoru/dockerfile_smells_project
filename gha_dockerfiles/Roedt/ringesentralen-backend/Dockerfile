# Step 1: build the native image
FROM ghcr.io/graalvm/graalvm-ce:java11-21.0.0 as graalvm
COPY . /home/app
WORKDIR /home/app

# Download and install Maven
ARG DBUSER
ARG DBPASSWORD
ARG QuarkusMailerUsername
ARG QuarkusMailerPassword
ARG MAVEN_VERSION=3.6.3
ARG USER_HOME_DIR="/root"
ARG SHA=c35a1803a6e70a126e80b2b3ae33eed961f83ed74d18fcd16909b2d44d7dada3203f1ffe726c17ef8dcca2dcaa9fca676987befeadc9b9f759967a8cb77181c0
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries

RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-maven-${MAVEN_VERSION}-bin.tar.gz \
  && echo "${SHA}  /tmp/apache-maven.tar.gz" | sha512sum -c - \
  && tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV GRAALVM_HOME $JAVA_HOME
RUN ${GRAALVM_HOME}/bin/gu install native-image

RUN $MAVEN_HOME/bin/mvn clean package -Pnative -B -e -Dquarkus.datasource.username=${DBUSER} -Dquarkus.datasource.password=${DBPASSWORD} -Dquarkus.mailer.username=${QuarkusMailerUsername} -Dquarkus.mailer.password=${QuarkusMailerPassword}

# Step 2: build the running container
FROM registry.fedoraproject.org/fedora-minimal
WORKDIR /work/
COPY --from=graalvm /home/app/target/*-runner /work/application
RUN chmod 775 /work
EXPOSE 8080
ENTRYPOINT ["./application", "-Dquarkus.http.host=0.0.0.0"]
