FROM maven
COPY target/ .
CMD java -jar -Dspring.profiles.active=mysql *.jar