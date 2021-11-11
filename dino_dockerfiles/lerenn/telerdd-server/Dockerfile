FROM debian:latest
MAINTAINER Louis Fradin <louis.fradin@gmail.com>

# Ports
EXPOSE 8080

# Volumes
VOLUME /var/log
VOLUME /nightwall-server

# Workdir
WORKDIR /nightwall-server

# Command
CMD ./bin/nightwall-server

# Data
COPY ./ ./
