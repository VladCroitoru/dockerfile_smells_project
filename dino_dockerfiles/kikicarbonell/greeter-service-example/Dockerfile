FROM nightscape/docker-sbt:latest

MAINTAINER Daniel Rhoades <daniel@danielrhoades.com>

# Create a user to run the microservice
RUN adduser -S microservice

WORKDIR /home/microservice

# Copy the microservice to the image
ADD . /home/microservice/

RUN sbt compile && \
    sbt assembly

EXPOSE 9000

# Run the microservice
USER microservice
CMD ["java", "-jar", "target/scala-2.11/greeter-service-example-assembly-0.1.jar"]
