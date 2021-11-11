FROM java:8

ENV STORAGE_BACKEND     memory
ENV STORAGE_PORT        10000
ENV STORAGE_FILE_PATH   /tmp/fileStorage

EXPOSE 10000

COPY . /usr/src/filestore

WORKDIR /usr/src/filestore

RUN ./gradlew fatjar

CMD ["java", "-jar", "build/libs/fileStore-all-0.4.2.jar"]
