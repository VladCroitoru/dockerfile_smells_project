FROM kmallea/steamcmd

MAINTAINER Kai Mallea <kmallea@gmail.com>

# Install CS:GO
RUN mkdir /opt/csgo &&\
    cd /opt/steamcmd &&\
    ./steamcmd.sh \
        +login anonymous \
        +force_install_dir /opt/csgo \
        +app_update 740 validate \
        +quit

# Make server port available to host
EXPOSE 27015

# This container will be executable
WORKDIR /opt/csgo
ENTRYPOINT ["./srcds_run"]
