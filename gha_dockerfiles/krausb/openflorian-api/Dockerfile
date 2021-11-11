# openflorian docker image
# based on tesseract 4 runtime environment
# additionals:
# - java 11
FROM $baseimage

RUN apt-get update
RUN apt-get install --fix-missing -y openjdk-11-jdk
RUN apt-get install --fix-missing -y curl

WORKDIR /

VOLUME /tmp
ARG DEPENDENCY=target/dependency
COPY ${DEPENDENCY}/BOOT-INF/lib /app/lib
COPY ${DEPENDENCY}/META-INF /app/META-INF
COPY ${DEPENDENCY}/BOOT-INF/classes /app
ENTRYPOINT ["java","-cp","app:app/lib/*","de.openflorian.OpenflorianApplication"]