FROM	debian:jessie-backports
MAINTAINER	thinkjd@thinkjd.de

# install dependencys
RUN	apt-get update && apt-get install -y wget
RUN	echo "deb http://overviewer.org/debian ./" >> /etc/apt/sources.list
RUN 	wget -O - http://overviewer.org/debian/overviewer.gpg.asc | apt-key add -
RUN	apt-get update && apt-get install -y minecraft-overviewer && apt-get clean

# setup env
RUN	mkdir /var/minecraft-overviewer && \
		cd /var/minecraft-overviewer && \
		mkdir world map
COPY	minecraft-overviewer.config /var/minecraft-overviewer/
COPY	render-and-generate-poi.sh /root/
RUN	chmod +x /root/render-and-generate-poi.sh

# get mc server jar for missing textures
RUN	wget https://s3.amazonaws.com/Minecraft.Download/versions/1.8/1.8.jar -P ~/.minecraft/versions/1.8/

VOLUME	["/var/minecraft-overviewer/world", "/var/minecraft-overviewer/map"]
ENTRYPOINT	["/root/render-and-generate-poi.sh"]
