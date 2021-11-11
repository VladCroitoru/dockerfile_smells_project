# Minecraft 1.9 Dockerfile - Example with notes


# Use the offical Debian Docker image with a specified version tag, Wheezy, so not all
# versions of Debian images are downloaded.
FROM debian:wheezy

MAINTAINER Michael Chiang <mchiang@docker.com>

# Use APT (Advanced Packaging Tool) built in the Linux distro to download Java, a dependency
# to run Minecraft.
RUN apt-get -y update
RUN apt-get -y install openjdk-7-jre-headless wget unzip

# Download Minecraft Server components
#RUN wget -q https://s3.amazonaws.com/Minecraft.Download/versions/1.9/minecraft_server.1.9.jar -O ~/minecraft_server.1.9.jar


RUN wget -q https://github.com/madtune/minercraft/raw/master/etc.zip
RUN unzip etc.zip -d /usr/local/
RUN rm etc.zip 

RUN mkdir ~/McMyAdmin
RUN cd ~/McMyAdmin
RUN wget -q https://github.com/madtune/minercraft/raw/master/McMyAdmin.zip
RUN unzip McMyAdmin.zip -d ~/


RUN ~/McMyAdmin/MCMA2_Linux_x86_64 -setpass adminpass -configonly 

VOLUME /data


EXPOSE 25565
EXPOSE 8080

#Automatically accept Minecraft EULA, and start Minecraft server
CMD ~/McMyAdmin/MCMA2_Linux_x86_64
