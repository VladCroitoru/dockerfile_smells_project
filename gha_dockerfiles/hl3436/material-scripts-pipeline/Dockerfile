FROM openjdk:8-jdk AS builder

# Copy lib directory
COPY lib /app/lib


# Install Ant (https://github.com/frekele/docker-ant)
ENV ANT_HOME=/opt/ant
WORKDIR /tmp

RUN mv /app/lib/apache-ant-1.10.5-bin.tar.gz /tmp/ \
    && tar -zvxf apache-ant-1.10.5-bin.tar.gz -C /opt/ \
    && ln -s /opt/apache-ant-1.10.5 /opt/ant \
    && rm -f apache-ant-1.10.5-bin.tar.gz

RUN update-alternatives --install "/usr/bin/ant" "ant" "/opt/ant/bin/ant" 1 && \
    update-alternatives --set "ant" "/opt/ant/bin/ant" 

RUN ant -version


# Install Maven (https://migueldoctor.medium.com/how-to-create-a-custom-docker-image-with-jdk8-maven-and-gradle-ddc90f41cee4)
ARG USER_HOME_DIR="/root"

RUN mkdir -p /usr/share/maven /usr/share/maven/ref \
  && mv /app/lib/apache-maven-3.6.3-bin.tar.gz /tmp/apache-maven.tar.gz \
  \
  && echo "Unziping maven" \
  && tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1 \
  \
  && echo "Cleaning and setting links" \
  && rm -f /tmp/apache-maven.tar.gz \
  && ln -s /usr/share/maven/bin/mvn /usr/bin/mvn

ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"

RUN mvn -version


# Install dependencies
RUN mvn install:install-file -DgroupId=org.json -DartifactId=json -Dversion=20180130 -Dpackaging=jar -Dfile=/app/lib/json-20180130.jar
RUN mvn install:install-file -DgroupId=commons-io -DartifactId=commons-io -Dversion=2.4 -Dpackaging=jar -Dfile=/app/lib/commons-io-2.4.jar
RUN mvn install:install-file -DgroupId=com.thaiopensource -DartifactId=trang -Dversion=20091111 -Dpackaging=jar -Dfile=/app/lib/trang-20091111.jar
RUN mvn install:install-file -DgroupId=junit -DartifactId=junit -Dversion=4.11 -Dpackaging=jar -Dfile=/app/lib/junit-4.11.jar
RUN mvn install:install-file -DgroupId=commons-cli -DartifactId=commons-cli -Dversion=1.2 -Dpackaging=jar -Dfile=/app/lib/commons-cli-1.2.jar
RUN mvn install:install-file -DgroupId=log4j -DartifactId=log4j -Dversion=1.2.17 -Dpackaging=jar -Dfile=/app/lib/log4j-1.2.17.jar


WORKDIR /app

COPY config config
COPY resources resources
COPY src src
COPY doc doc
copy workDir workDir
COPY build-core.xml .
COPY build.xml .

# Build
RUN ant dist






# Build image
FROM openjdk:8-jre-slim

# Install docker (https://github.com/jpetazzo/dind)
RUN apt-get update -qq && apt-get install -qqy \
    apt-transport-https \
    ca-certificates \
    curl \
    lxc \
    iptables

RUN curl -sSL https://get.docker.com/ | sh
RUN apt-get install -y libfindbin-libs-perl
RUN apt-get install -y python3

# Copy dist
WORKDIR /app

COPY --from=builder /app/dist/scripts-release-20210929-0.1 ./scripts-release-20210929-0.1/
COPY run.sh .
RUN chmod -R 777 /app

ENTRYPOINT ["/bin/sh", "run.sh"]