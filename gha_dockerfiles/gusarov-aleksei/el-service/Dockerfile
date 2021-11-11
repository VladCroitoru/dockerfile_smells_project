FROM bellsoft/liberica-openjdk-alpine:11.0.12-7 as el-service
RUN apk add --no-cache --upgrade bash && apk add --no-cache --upgrade curl
COPY run.sh target/QJ-1.0-SNAPSHOT-runner.jar ./
RUN chmod +x run.sh
EXPOSE 8080
CMD ./run.sh
#CMD ["java", "-jar","QJ-1.0-SNAPSHOT-runner.jar"]