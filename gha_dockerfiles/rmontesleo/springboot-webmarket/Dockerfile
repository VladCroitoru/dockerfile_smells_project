FROM openjdk:11

# Create app directory
WORKDIR /usr/src/app

ADD target/market-api.jar /usr/src/app/market-api.jar

EXPOSE 80
ENTRYPOINT [ "java", "-jar", "-Dspring.profiles.active=pdn", "market-api.jar" ]