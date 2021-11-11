# Permet de construire notre image à partir de Java 8
FROM openjdk:8-jre-alpine

# Equivalent de "docker run -v" pour créer un autre volume de destination
# On copie nos fichiers locaux dans le container
# Comme nous avons récupérer les sources JS on les copier dans le container
COPY . /coocotte

ENV JHIPSTER_SLEEP 0

# Renomme le package war
ADD target/*.war /app.war

# On modifie la date de modification pour que docker le prenne en compte
RUN sh -c 'touch /app.war'

# Spring Boot travaille dans ce dossier au besoin
VOLUME /tmp

# Container ecoute le port 8080 (bien ajouté -p dans le docker run pour le rendre accessible)
EXPOSE 8080

CMD echo "The application will start in ${JHIPSTER_SLEEP}s..." && \
   sleep ${JHIPSTER_SLEEP}

# Djava.security.egd=file:/dev/./urandom permet de reduire le temps de démarrage de tomcat
ENV JAVA_OPTS=""
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS -Djava.security.egd=file:/dev/./urandom -jar /app.war" ]