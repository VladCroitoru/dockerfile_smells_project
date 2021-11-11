FROM openjdk:16

MAINTAINER Florian Weber <florian.florianweber.weber@gmail.com>

ADD backend/target/photohunter.jar app.jar

CMD [ "sh", "-c", "java -Dserver.port=$PORT -Dspring.data.mongodb.uri=$MONGO_DB_URI  -jar /app.jar" ]
