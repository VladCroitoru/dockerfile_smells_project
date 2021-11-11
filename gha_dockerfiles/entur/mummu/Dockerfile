FROM adoptopenjdk/openjdk11:alpine-jre
WORKDIR /deployments
COPY target/mummu-*-SNAPSHOT.jar /deployments/mummu.jar

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod a+x /docker-entrypoint.sh
ENTRYPOINT ["sh", "/docker-entrypoint.sh"]

RUN addgroup appuser && adduser --disabled-password appuser --ingroup appuser
RUN chown -R appuser:appuser /deployments
USER appuser

CMD java $JAVA_OPTIONS -jar /deployments/mummu.jar