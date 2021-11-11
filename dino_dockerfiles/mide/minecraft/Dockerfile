FROM openjdk:jre

MAINTAINER Mark Ide Jr (https://www.mide.io)

# Install the needed packages
RUN apt-get update && \
    apt-get -y install wget python3 && \
    rm -rf /var/lib/apt/lists/*

# Default JVM Options (Set default memory limit to 1G)
ENV JAVA_TOOL_OPTIONS "-Xmx1024M -Xms1024M"

# Add Minecraft user
WORKDIR "/minecraft"

# Copy all the scripts into the container
RUN mkdir -p /minecraft-scripts/
COPY scripts/healthcheck.py /minecraft-scripts/healthcheck.py
COPY scripts/minecraft_rcon.py /minecraft-scripts/minecraft_rcon.py
COPY scripts/server_properties.py /minecraft-scripts/server_properties.py
COPY scripts/wrapper.py /minecraft-scripts/wrapper.py

RUN chmod +x /minecraft-scripts/healthcheck.py && \
    chmod +x /minecraft-scripts/wrapper.py

ENTRYPOINT ["/minecraft-scripts/wrapper.py"]

# HEALTHCHECK CMD --start-period=300 ["/minecraft-scripts/healthcheck.py"]
