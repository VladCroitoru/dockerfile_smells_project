
FROM java:8
MAINTAINER Toon Sevrin <twan123@live.be>

# Create user to run spigot as, this will make sure permissions work as well
RUN useradd -s /bin/bash -d /opt/mcserver -m minecraft

# Install rsync that will allow us to sync from volumes
RUN apt-get update && apt-get install -y curl rsync tmux && rm -rf /var/lib/apt/lists/* \

# Create location for the server jars and plugins
VOLUME ["/opt/minecraft"]

# Exposes local port, must be exposed publically with -p xxxx:25565
EXPOSE 25565

# Copy the execution script, make sure it can be executed and set it as entrypoint
COPY ./spigot /usr/local/bin/
RUN chmod a+x /usr/local/bin/spigot
ENTRYPOINT ["/usr/local/bin/spigot"]
