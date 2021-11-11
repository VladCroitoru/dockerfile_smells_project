FROM alpine:latest

RUN apk --no-cache add openjdk11-jdk

COPY target/scala-2.13/generate-pdf.jar /bin

CMD java $JAVA_OPTS -jar /bin/generate-pdf.jar