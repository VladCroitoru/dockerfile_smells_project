FROM openjdk:11-jre-slim-sid

ARG ARTIFACT_VERSION

ENV ARTIFACT enquiry-handler-${ARTIFACT_VERSION}.jar

EXPOSE 8080

COPY /target/${ARTIFACT} /opt/${ARTIFACT}

CMD java -Xms50m -Xmx100m \
    -Dspring.config.additional-location=file:/etc/config/ \
    -Duser.timezone=UTC \
    -jar /opt/${ARTIFACT}
