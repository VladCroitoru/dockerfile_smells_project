
# We start from the offical Java image base
FROM java:8

MAINTAINER EMCDotNextTeam
# dotnext@emc.com

# Create a directory 
#   /app for the java program

RUN  mkdir /app
RUN curl "https://s3.amazonaws.com/Minecraft.Download/versions/1.10.2/minecraft_server.1.10.2.jar" -o /app/minecraft_server.jar

# Minecraft requries an accepted eula to run
RUN  echo "eula=true" > /app/eula.txt

# Expose the default Minecraft server port
EXPOSE 25565

# add in a custom server.properties file that sets the world to the /data directory and turns off monsters (because I don't want to die while demo-ing :-)
COPY server.properties /app/

# set the working directory
WORKDIR /app

# start the server
ENTRYPOINT [ "java", "-Xmx1024M", "-Xms1024M", "-jar", "/app/minecraft_server.jar", "nogui" ]
