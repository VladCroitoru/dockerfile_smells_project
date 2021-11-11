FROM java:8
MAINTAINER Yanick Nedderhoff <yanicknedderhoff@gmail.com>

# Set the timezone.
RUN echo "Europe/Berlin" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

# Install maven
RUN apt-get update
RUN apt-get install -y maven --no-install-recommends
RUN apt-get clean

WORKDIR /code

# Prepare by downloading dependencies
COPY pom.xml /code/pom.xml
RUN ["mvn", "dependency:resolve"]
RUN ["mvn", "verify"]

# Adding source, compile and package into a fat jar
COPY src /code/src
RUN ["mvn", "package"]

COPY start.sh /code/start.sh

ENTRYPOINT ["/bin/bash","start.sh"]
CMD ["-Dlog.level=DEBUG" "config.json" "15"]

