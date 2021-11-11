FROM adoptopenjdk/openjdk8
ARG JAR_FILE=target/*.jar
ENV BOT_NAME=test_hamza_bot
ENV BOT_TOKEN=1917018839:AAEHnN08qlE8LsyGoKewFGCwU-q57j8BKrM
ENV BOT_DB_USERNAME=postgres
ENV BOT_DB_PASSWORD=admin888
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java", "-Dspring.datasource.password=${BOT_DB_PASSWORD}", "-Dbot.username=${BOT_NAME}", "-Dbot.token=${BOT_TOKEN}", "-Dspring.datasource.username=${BOT_DB_USERNAME}", "-jar", "/app.jar"]