FROM tomcat:9.0-jdk16

ARG VERSION
COPY ./src/main/webapp/META-INF/maven/kakeibo/kakeibo/target/kakeibo-0.0.1-SNAPSHOT.war /usr/local/tomcat/webapps/kakeibo.war

CMD ["catalina.sh", "run"]




# FROM mcr.microsoft.com/java/jre:11-zulu-debian10

# ARG VERSION
# COPY ./target/program-${VERSION}.jar /opt
# RUN echo "#!/bin/bash\n\n\
# java -Dspring.profiles.active=production -jar program-${VERSION}.jar\n" >> /opt/batch.sh
# RUN chmod u+x /opt/batch.sh

# WORKDIR /opt
# CMD [ "/opt/batch.sh" ]
