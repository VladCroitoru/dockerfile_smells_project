FROM debian

LABEL maintainer="FMMT666 fmmt666@users.noreply.github.com"


RUN  apt-get -y update && \
     apt-get -y upgrade && \
     apt-get -y install cowsay fortune joe mc wget && \
     echo "alias d='ls -la --color'" >> /root/.bashrc && \
     wget -O tserver.zip "https://terraria.org/system/dedicated_servers/archives/000/000/045/original/terraria-server-1422.zip" && \
     unzip tserver.zip && \
     rm tserver.zip && \
     rm -rf /1422/Mac && \
     rm -rf /1422/Windows &&\
     chmod +x '/1422/Linux/TerrariaServer.bin.x86_64' && \
     wget -O tservermobile.zip "https://terraria.org/server/MobileTerrariaServer.zip" && \
     unzip tservermobile.zip &&\
     rm tservermobile.zip &&\
     rm OSX_* &&\
     rm Windows_* &&\
     unzip Linux_*.zip &&\
     rm Linux_*.zip &&\
     chmod +x '/ServerLinux/TerrariaServer.bin.x86_64'

VOLUME /terraria

COPY runthis.sh       /
COPY serverconfig.txt /

ENTRYPOINT ["/runthis.sh"]
