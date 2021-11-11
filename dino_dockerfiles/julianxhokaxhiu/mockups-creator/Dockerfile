FROM finalduty/archlinux
MAINTAINER Julian Xhokaxhiu < info at julianxhokaxhiu dot com >

# Environment variables
#######################

ENV DATA_DIR /app

# Configurable environment variables
####################################

# Set to false to enable development mode
ENV PRODUCTION true

# Create Volume entry points
############################

VOLUME $DATA_DIR

# Copy required files and fix permissions
#########################################

COPY Dockerfile_src/* /opt/

# Create missing directories
############################

RUN mkdir -p $DATA_DIR \
    && mkdir -p /opt

# Set the work directory
########################

WORKDIR /opt

# Fix permissions
#################

RUN chmod 0644 * \
    && chmod 0755 *.sh

# Install required packages
##############################
RUN yes '' | pacman -Sy --noprogressbar --noconfirm --needed git wget fontforge nodejs npm jre8-openjdk java-batik \
    && npm install -g ttf2eot ttf2svg grunt-cli \
    && wget http://ftp-stud.hs-esslingen.de/pub/Mirrors/ftp.apache.org/dist/xmlgraphics/batik/binaries/batik-bin-1.8.tar.gz -P /opt \
    && tar xzf /opt/batik-bin-1.8.tar.gz -C /usr/share/java \
    && rm /opt/batik-bin-1.8.tar.gz \
    && echo -e '#!/bin/bash\n\java -Djava.awt.headless=true -jar /usr/share/java/batik-1.8/batik-ttf2svg-1.8.jar "$@"\n' > /usr/local/bin/batik-ttf2svg \
    && chmod 0755 /usr/local/bin/batik-ttf2svg \
    && chown root:root /usr/local/bin/batik-ttf2svg

# Cleanup
#########

RUN yes | pacman -Scc

# Expose required ports
#######################

EXPOSE 8080

# Set the entry point to init.sh
###########################################

ENTRYPOINT /opt/init.sh