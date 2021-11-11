# CS GO Server
#
# Version 0.1

FROM centos
MAINTAINER Ludwig Bayerlein

LABEL DESCRIPTION="This images creates a Counter Strike Global Offensive Server"

RUN yum update -y && \
    yum install glibc.i686 libstdc++ libstdc++.i686 wget -y

RUN mkdir /opt/csgo && \
    cd /opt/csgo && \
    wget http://media.steampowered.com/installer/steamcmd_linux.tar.gz && \
    tar -xvzf steamcmd_linux.tar.gz

RUN /opt/csgo/steamcmd.sh +login anonymous \
                          +force_install_dir /opt/csgo/csgoserver \
                          +app_update 740 validate \
                          +quit

#ADD Default config files
RUN yum install unzip -y
ADD server.cfg /opt/csgo/csgoserver/csgo/cfg/
RUN cd /opt/csgo/csgoserver/csgo/cfg && wget http://gfx.esl.eu/media/counterstrike/csgo/downloads/configs/csgo_esl_serverconfig.zip && unzip csgo_esl_serverconfig.zip

# Make port available
EXPOSE 27015

# This container will be executable
WORKDIR /opt/csgo/csgoserver
#ENTRYPOINT ["./srcds_run -game csgo -usercon -strictportbind -ip 0.0.0.0 -p 27015"]
ENTRYPOINT ["./srcds_run"]

