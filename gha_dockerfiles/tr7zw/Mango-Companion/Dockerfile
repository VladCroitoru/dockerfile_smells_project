FROM adoptopenjdk/openjdk11-openj9:alpine-slim

WORKDIR /companion

COPY target/*-jar-with-dependencies.jar ./mango-companion.jar
COPY webapp/style.css ./webapp/style.css
COPY webapp/WEB-INF/web.xml ./webapp/WEB-INF/web.xml

CMD ["java", "-jar", "mango-companion.jar", "/library"]