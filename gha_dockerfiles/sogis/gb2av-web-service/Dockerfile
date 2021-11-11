FROM adoptopenjdk/openjdk11:latest

USER root

RUN apt-get update && apt-get install -y --no-install-recommends libfontconfig1 && rm -rf /var/lib/apt/lists/*

WORKDIR /home/gb2av
COPY build/libs/*.jar /home/gb2av/gb2av-web-service.jar
RUN cd /home/gb2av && \
    chown -R 0 /home/gb2av && \
    chmod -R g+rw /home/gb2av && \
    ls -la /home/gb2av

ENV ILI_CACHE=/home/gb2av

EXPOSE 8080

CMD java -XX:MaxRAMPercentage=80.0 -jar gb2av-web-service.jar 
