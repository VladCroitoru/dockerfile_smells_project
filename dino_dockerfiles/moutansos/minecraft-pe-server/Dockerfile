FROM alpine

# Create the data directory and add the EULA
VOLUME ["/data"]
RUN echo eula=true > /data/eula.txt

#Update and install packages
RUN apk update
RUN apk add ca-certificates openssl openjdk8
RUN update-ca-certificates

#Download minecraft
RUN wget -O /srv/minecraft-pe-server.jar http://ci.mengcraft.com:8080/job/nukkit/lastStableBuild/artifact/target/nukkit-1.0-SNAPSHOT.jar

#Open the necessary port
EXPOSE 25565

#Start everything on runtime
CMD echo eula=true > /data/eula.txt && cd /data && /bin/sh -c "java -Xmx1024M -Xms1024M -jar /srv/minecraft-pe-server.jar" > /data/server.log
