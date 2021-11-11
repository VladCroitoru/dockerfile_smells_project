from dockerfile/java
MAINTAINER Johnny Bergström <docker@joonix.se>

# Create a user and home directory which YouTrack will put its database into
RUN useradd -m youtrack
WORKDIR /home/youtrack

# Download the actual YouTrack application
RUN wget -q http://download.jetbrains.com/charisma/youtrack-5.2-8723.jar -O youtrack.jar

# Configure logging to use stdout
ADD log4j.xml /home/youtrack/

# Use a volume for the database files
VOLUME /home/youtrack/teamsysdata

ENTRYPOINT ["su", "-l", "youtrack", "-c"]
CMD ["java -Xmx512m -XX:MaxPermSize=150m -Djetbrains.mps.webr.log4jPath=/home/youtrack/log4j.xml -Djava.awt.headless=true -jar youtrack.jar 8080"]

EXPOSE 8080