FROM maven:3.5-jdk-8 as BUILD
WORKDIR /build

#optimize for reusing local cache during builds
ADD ./pom.xml /build/pom.xml
RUN mvn package
