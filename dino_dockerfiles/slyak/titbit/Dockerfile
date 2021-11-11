FROM openjdk:8
RUN apt-get install git && \
    git clone https://github.com/stormning/titbit.git
RUN cd /titbit && ./mvnw install
VOLUME /opt/data/titbit
ENTRYPOINT java -Djava.security.egd=file:/dev/./urandom -jar /titbit/titbit-service/target/titbit-service-0.0.1-SNAPSHOT.jar