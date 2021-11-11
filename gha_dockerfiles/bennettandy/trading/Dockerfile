FROM adoptopenjdk/openjdk11:alpine-jre

 # Refer to Maven build -> finalName
 ARG JAR_FILE=./build/libs/trading-0.0.1.jar

 # cd /opt/app
 WORKDIR /opt/app

 # cp target/{jarfileName}.jar /opt/app/app.jar
 COPY ${JAR_FILE} app.jar

 # java -jar /opt/app/app.jar
 ENTRYPOINT ["java","-jar","app.jar"]
