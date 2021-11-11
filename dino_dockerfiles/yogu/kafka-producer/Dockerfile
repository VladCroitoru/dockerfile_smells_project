FROM maven:3.2.5-jdk-8u40

RUN mkdir --parents /usr/src/app
WORKDIR /usr/src/app

# selectively add the POM file
ADD pom.xml /usr/src/app/
# get all the downloads out of the way
RUN mvn verify clean --fail-never

ADD . /usr/src/app
RUN mvn package

CMD java -jar target/service-jar-with-dependencies.jar
