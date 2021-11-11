from centos:centos6

MAINTAINER Ben Hosmer <ben.hosmer@gmail.com>

ENV MCVERSION 1.8 

# Add the overviewer repository, EPEL, and install overviewer.
RUN yum install -y wget && wget -O /etc/yum.repos.d/overviewer.repo http://overviewer.org/rpms/overviewer.repo && rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm && yum -y update && yum -y install Minecraft-Overviewer 

ADD overviewer.cfg /overviewer.cfg

VOLUME = ['/world']
VOLUME = ['/maps']

# Now build the maps
CMD wget https://s3.amazonaws.com/Minecraft.Download/versions/$MCVERSION/$MCVERSION.jar -P /root/.minecraft/versions/$MCVERSION/ && /usr/bin/overviewer.py -c overviewer.cfg

