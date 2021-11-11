FROM alpine

# Create the data directory and add the EULA
VOLUME ["/data"]
RUN echo eula=true > /data/eula.txt

#Update and install packages
RUN apk update
RUN apk add ca-certificates openssl openjdk8
RUN update-ca-certificates

#Download minecraft
RUN wget -O /srv/minecraft-server.jar https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar

#Open the necessary port
EXPOSE 25565

#Start everything on runtime
CMD echo eula=true > /data/eula.txt && cd /data && /bin/sh -c "java -Xmx4024M -Xms1024M -jar /srv/minecraft-server.jar nogui" > /data/server.log
