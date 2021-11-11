FROM debian:testing
MAINTAINER Jonathan David Page <jonathan@sleepingcyb.org>

# install us some java and python
RUN apt-get update \
 && apt-get install -y default-jre-headless \
                       python3 \
                       python3-pip \
 && apt-get clean

# add the required python packages
ADD requirements.txt /opt/minecraft/
RUN pip3 install -r /opt/minecraft/requirements.txt

# grab the minecraft server
ADD https://s3.amazonaws.com/Minecraft.Download/versions/1.8.4/minecraft_server.1.8.4.jar /opt/minecraft/

# add the mchttpinfowrapper sources
ADD . /opt/minecraft

# expose minecraft to the world
EXPOSE 25565 8088

VOLUME ["/opt/minecraft/server"]

CMD cd /opt/minecraft && ./bin/mchttpinfowrapper
