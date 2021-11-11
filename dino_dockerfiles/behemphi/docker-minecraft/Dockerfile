# We are starting from BusyBox to keep the image size as small as possible
FROM jeanblanchard/busybox-java:8

# Java and Minecraft are independently fast moving targets, let's see how I do 
# trying to keep up.  Please reach out if an update is needed.
MAINTAINER Boyd Hemphill <behemphi@gmail.com>

# Set the version of the Minecraft server for this build. 
ENV VERSION="15w42a"

# Set the default port. This can be sensibly overwritten at run time.
ENV PORT 25565

# Tell the image to expect an external volume for data
# VOLUME /minecraftdata

# We are going to put our MineCraft JAR in its own special directory
WORKDIR /minecraft

# flag must be explicitly set in the run command for this port to 
# be exposed by the container
EXPOSE ${PORT}

# The EULA is a file that is written out the first time the server is started 
# only if it does not exist. We are going to drop the needed KV pair and
# call it good. This happens at config time because we don't want to deal with 
# it on every run.
RUN echo "eula=true" > eula.txt

# Below is an abstraction of properties found in the 
# server.properties file. We are going define them here with their 
# defaults, as a way to allow the user of this container to change
# the _configuration time_ settings of the server.  
#
# Changing the configuration properties of the server at run time 
# is enabled through the start.sh script. Unlike the EULA, we must enable
# run time server config so users don't have know about rebuilding a container
# each time they want to change a setting.
#
# List of properties found here: 
#   http://minecraft.gamepedia.com/Server.properties
#
# Note the use of a single ENV command. This makes for far fewer layers
# in the image.
ENV SPAWN_PROTECTION=16                 MAX_TICK_TIME=-1 \
    GENERATOR_SETTINGS=""               FORCE_GAMEMODE=false \
    ALLOW_NETHER=true                   GAMEMODE=0 \
    ENABLE_QUERY=false                  PLAYER_IDLE_TIMEOUT=0 \
    DIFFICULTY=1                        SPAWN_MONSTERS=true \
    OP_PERMISSION_LEVEL=4               RESOURCE_PACK_HASH="" \
    ANNOUNCE_PLAYER_ACHIEVEMENTS=true   PVP=true \
    SNOOPER_ENABLED=true                LEVEL_TYPE=DEFAULT \
    HARDCORE=false                      ENABLE_COMMAND_BLOCK=false \
    MAX_PLAYERS=20                      NETWORK_COMPRESSION_THRESHOLD=256 \
    MAX_WORLD_SIZE=29999984             SERVER_PORT=25565 \
    SERVER_IP=""                        SPAWN_NPCS=true \
    ALLOW_FLIGHT=false                  LEVEL_NAME=WORLD \
    VIEW_DISTANCE=10                    RESOURCE_PACK="" \
    SPAWN_ANIMALS=true                  WHITE_LIST=false \
    GENERATE_STRUCTURES=true            ONLINE_MODE=true \
    MAX_BUILD_HEIGHT=256                LEVEL_SEED="" \
    USE_NATIVE_TRANSPORT=true           ENABLE_RCON=false \
    MOTD="Welcome to my very own Minecraft server!" \
    QUERY_PORT=25565                    RCON_PASSWORD="" \
    RCON_PORT=25575                    

# These next two are not server.properties values, rather they configure 
# memory allocation for the JVM itself. We want these to be set sensibly, but 
# to allow for changes if a user decides to scale up/down.
#
# Because this file is tied to a blogpost suggesting a 1GB droplet at 
# Digital Ocean, we will deviate from the normal 1024M
ENV MAX_MEM_POOL=768                   INITIAL_MEM_POOL=768

# Add the start script from the local directory. This assumes you have cloned
# the repo locally and are building accordingly
ADD start.sh start.sh
RUN chmod +x start.sh

# Some logs are written to file even though they are also written to STDERR and 
# STDOUT. We are going to send those to /dev/null
RUN mkdir logs

# Expose the typical Minecraft server port. Remember however that the -P 
# Pull in the Minecraft server jar based on version
# This happens towards the end to keep the above command hitting the docker 
# build cache and speeding up the process.
ADD https://s3.amazonaws.com/Minecraft.Download/versions/${VERSION}/minecraft_server.${VERSION}.jar minecraft_server.jar
#ADD minecraft_server.1.8.6.jar minecraft_server.jar

# Place the template file for server.properties. This is assumed to be in the
# local directory.
ADD server.properties.template server.properties.template

# Run the server. Once past the EULA it will write out some new files.  
ENTRYPOINT ["/minecraft/start.sh"]

