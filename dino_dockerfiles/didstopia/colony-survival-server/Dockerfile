# Builder image
FROM golang:1.15 as builder
RUN go get -v github.com/Didstopia/steamer
WORKDIR /go/src/github.com/Didstopia/steamer/
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o steamer .
#RUN steamer --appinfo 748090



# Primary image
FROM didstopia/base:steamcmd-ubuntu-18.04

LABEL maintainer="Didstopia <support@didstopia.com>"

# Fixes apt-get warnings
ARG DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN add-apt-repository ppa:longsleep/golang-backports && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
    net-tools \
    jq \
    cron \
    libsdl2-2.0-0:i386 \
    rsyslog && \
	rm -rf /var/lib/apt/lists/*

# Create and set the steamcmd folder as a volume
RUN mkdir -p /steamcmd/colonysurvival
VOLUME ["/steamcmd/colonysurvival"]

# Add the steamcmd installation script
ADD install.txt /app/install.txt

# Copy any scripts
ADD start.sh /app/start.sh
ADD update.sh /app/update.sh

# Make sure they're executable
RUN chmod +x /app/*.sh

# Copy the compiled Go app
COPY --from=builder /go/src/github.com/Didstopia/steamer/steamer /usr/bin

# Add the crontab
ADD crontab /app/update.cron

# Set the current working directory
WORKDIR /

# Expose necessary ports
#EXPOSE 27004/tcp
#EXPOSE 27004/udp
EXPOSE 27016/tcp
EXPOSE 27016/udp
EXPOSE 27017/tcp

# Run as a non-root user by default
ENV PGID 1000
ENV PUID 1000

# Enable passwordless sudo
ENV ENABLE_PASSWORDLESS_SUDO "true"

# Setup default environment variables for the server
ENV SERVER_STARTUP_ARGS "-batchmode -nographics start_server +server.gameport 27016 +server.steamport 27017 +server.networktype SteamOnline +server.usevac true"
ENV SERVER_NAME "Docker"
ENV SERVER_PASSWORD ""

# Test that the Go app works
#RUN steamer --appinfo 748090

# Start the server
CMD [ "/bin/bash", "/app/start.sh"]
