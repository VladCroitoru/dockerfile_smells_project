# -----------------------------------------------------------------------------
# This is base image of Ubuntu LTS with SSHD service.
#
# Authors: Art567
# Updated: Sep 20th, 2015
# Require: Docker (http://www.docker.io/)
# -----------------------------------------------------------------------------


# Base system is the latest LTS version of Ubuntu.
from   tensorflow/tensorflow:latest


# Make sure we don't get notifications we can't answer during building.
env    DEBIAN_FRONTEND noninteractive


# Prepare scripts and configs
add    ./scripts/start /start


# Download and install everything from the repos.
run    apt-get -q -y update; apt-get -q -y upgrade && \
       apt-get -q -y install sudo openssh-server vim net-tools&& \
       mkdir /var/run/sshd


# Set root password
run    echo 'root:password' >> /root/passwdfile


# Create user and it's password
run    useradd -m -G sudo mason && \
       echo 'mason:password' >> /root/passwdfile


# Apply root password
run    chpasswd -c SHA512 < /root/passwdfile && \
       rm /root/passwdfile


RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    sed -ri 's/Port 22/Port 2222/g' /etc/ssh/sshd_config 

# Port 22 is used for ssh
expose 2222


# Assign /data as static volume.
volume ["/data"]


# Fix all permissions
run    chmod +x /start


# Starting sshd
cmd    ["/start"]

USER mason

#nvidia-docker run -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY -it -d 
