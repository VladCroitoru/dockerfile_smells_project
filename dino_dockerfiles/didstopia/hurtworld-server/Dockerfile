FROM didstopia/base:nodejs-steamcmd-ubuntu-16.04

LABEL maintainer="Didstopia <support@didstopia.com>"

# Fixes apt-get warnings
ARG DEBIAN_FRONTEND=noninteractive

# Run a quick apt-get update/upgrade
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y

# Install dependencies
RUN apt-get install --no-install-recommends -y \
    telnet

# Run as root
USER root

# Setup the default timezone
ENV TZ=Europe/Helsinki
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Create and set the steamcmd folder as a volume
RUN mkdir -p /steamcmd/hurtworld
VOLUME ["/steamcmd/hurtworld"]

# Add the steamcmd installation script
ADD install.txt /install.txt

# Copy startup script
ADD start_hurtworld.sh /start.sh

# Expose necessary ports
EXPOSE 12871
EXPOSE 12871/udp
EXPOSE 12881/udp

# Setup default environment variables for the server
ENV HURTWORLD_SERVER_STARTUP_EXEC "host 12871;queryport 12881;servername Hurtworld [DOCKER];maxplayers 16"
ENV HURTWORLD_SERVER_STARTUP_ARGUMENTS "-batchmode -nographics -logfile /dev/stdout"

# Start the server
ENTRYPOINT ["./start.sh"]
