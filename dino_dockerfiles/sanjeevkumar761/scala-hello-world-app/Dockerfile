FROM openjdk:8

RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY ./run_jar.sh ./app-assembly.jar ./
EXPOSE 9000
ENTRYPOINT ["./run_jar.sh"]

