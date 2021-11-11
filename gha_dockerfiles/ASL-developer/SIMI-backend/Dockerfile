# STAGE #1
# build maven project and generate jar
FROM openjdk:15-jdk-slim AS build

# Install Maven
ARG MAVEN_VERSION=3.6.3
ARG USER_HOME_DIR="/root"

RUN apt-get update && apt-get install -y curl tar && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /usr/share/maven && \
curl -fsSL http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz | tar -xzC /usr/share/maven --strip-components=1 && \
ln -s /usr/share/maven/bin/mvn /usr/bin/mvn
ENV MAVEN_HOME /usr/share/maven
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"
ENV MAVEN_OPTS="-XX:+TieredCompilation -XX:TieredStopAtLevel=1"
ENV TZ=Europe/Rome
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# copy source and package with maven
WORKDIR /app
COPY ./ ./
RUN mvn clean package

# STAGE #2 - copy jar and launch spring
FROM openjdk:15-jdk-slim
ENV TZ=Europe/Rome
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY --from=build /app/target/simi-backend.jar ./
EXPOSE 8080
ENTRYPOINT ["java","-jar","simi-backend.jar"]
