FROM maven:alpine
MAINTAINER hyness <hyness@freshlegacycode.org>

EXPOSE 8080
COPY . /opt/turbine-hystrix-dashboard/
WORKDIR /opt/turbine-hystrix-dashboard/
RUN mvn package
VOLUME /config
WORKDIR /
ENTRYPOINT ["java", "-Djava.security.egd=file:/dev/./urandom", "-jar",\
            "/opt/turbine-hystrix-dashboard/target/turbine-hystrix-dashboard.jar"]
