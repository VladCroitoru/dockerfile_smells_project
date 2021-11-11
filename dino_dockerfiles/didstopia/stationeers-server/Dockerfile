
FROM didstopia/base:nodejs-12-steamcmd-ubuntu-18.04

LABEL maintainer="Didstopia <support@didstopia.com>"

# Fixes apt-get warnings
ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libsdl2-2.0-0:i386 \
        net-tools && \
	rm -rf /var/lib/apt/lists/*

# Create and set the steamcmd folder as a volume
RUN mkdir -p /steamcmd/stationeers

# Add the steamcmd installation script
ADD install.txt /app/install.txt

# Copy the startup script
ADD start_stationeers.sh /app/start.sh

# Set the current working directory
WORKDIR /

# Setup default environment variables for the server
ENV STATIONEERS_SERVER_STARTUP_ARGUMENTS "-autostart -nographics -batchmode"
ENV STATIONEERS_SERVER_NAME "A Docker Server"
ENV STATIONEERS_WORLD_NAME "docker"
ENV STATIONEERS_SERVER_SAVE_INTERVAL "300"
ENV STATIONEERS_GAME_PORT "27500"
ENV STATIONEERS_QUERY_PORT "27015"
ENV STATIONEERS_SERVER_PASSWORD ""

# Run as a non-root user by default
ENV PGID 1000
ENV PUID 1000

# Expose necessary ports
EXPOSE 27500/tcp
EXPOSE 27500/udp
EXPOSE 27015/udp

# Define directories to take ownership of
ENV CHOWN_DIRS "/app,/steamcmd"

# Expose the volumes
# VOLUME ["/steamcmd/stationeers"]

# Start the server
CMD [ "bash", "/app/start.sh"]
