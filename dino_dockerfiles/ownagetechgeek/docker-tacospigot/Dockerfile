FROM nimmis/java:openjdk-8-jre-headless

MAINTAINER OwnageTechGeek <ownagetechgeek@talentcraft.net>
ENV DEBIAN_FRONTEND noninteractive
ENV PROCESSHOME /tacospigot
ENV INVOCATION 'java -Xms512M -Xmx1024M -Dcom.mojang.eula.agree=true -jar TacoSpigot.jar --world-dir worlds'
ADD start.sh /start.sh
RUN chmod +x /start.sh
RUN apt-get update
RUN apt-get clean all
RUN useradd -s /bin/bash -d /tacospigot -m tacospigot
CMD /start.sh
