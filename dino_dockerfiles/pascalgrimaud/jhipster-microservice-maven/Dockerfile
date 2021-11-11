FROM java:8

ENV JHIPSTER_SLEEP 0
ENV SPRING_PROFILES_ACTIVE=prod
ENV SPRING_DATASOURCE_URL=jdbc:mysql://mysql:3306/msmaven?useUnicode=true&characterEncoding=utf8&useSSL=false

# add source
ADD . code/
# package the application and delete all lib
RUN cd /code/ && \
    ./mvnw package -Pprod -DskipTests && \
    mv /code/target/*.war /app.war && \
    rm -Rf /code && \
    rm -Rf /root/.m2/wrapper && \
    rm -Rf /root/.m2/repository && \
    rm -Rf /root/.gradle && \
    rm -Rf /home/jhipster/.npm/

RUN sh -c 'touch /app.war'
VOLUME /tmp
EXPOSE 8081 5701/udp
CMD echo "The application will start in ${JHIPSTER_SLEEP}s..." && \
    sleep ${JHIPSTER_SLEEP} && \
    java -Djava.security.egd=file:/dev/./urandom -jar /app.war
