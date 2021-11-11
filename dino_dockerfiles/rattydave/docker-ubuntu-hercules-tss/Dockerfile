FROM	ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN	apt-get update && \
      apt-get install -y  unzip wget hercules mc screen && \
      cd /opt && \
      mkdir hercules && \
      cd hercules && \
      mkdir tss && \
      cd tss && \
      wget http://www.ibiblio.org/jmaynard/tss370r3.zip && \
      unzip tss370r3.zip && \
      rm tss370r3.zip && \
      echo "HTTPPORT       8038" >> /opt/hercules/tss/tss.cnf && \
      apt-get -y autoclean && apt-get -y autoremove && \
      echo "#!/bin/bash" > start_tss.sh && \
      echo "cd /opt/hercules/tss"  >> start_tss.sh && \
      echo "/usr/bin/screen -dm -S herc hercules -f tss.cnf"  >> start_tss.sh && \
      echo "/bin/sh" >> start_tss.sh && \
      chmod 755 start_tss.sh && \
      apt-get -y purge $(dpkg --get-selections | grep deinstall | sed s/deinstall//g) && \
      rm -rf /var/lib/apt/lists/*

EXPOSE      3270 8038
WORKDIR     /opt/hercules/tss
ENTRYPOINT  ["/opt/hercules/tss/start_tss.sh"]
