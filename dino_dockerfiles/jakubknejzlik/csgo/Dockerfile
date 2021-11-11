FROM ubuntu:16.04

ENV LAST_UPDATED_AT 2017-09-19

RUN apt-get update \
    # install dependencies
    && apt-get install -y lib32gcc1 curl lib32stdc++6 \
    # delete apt cache to save space
    && rm -rf /var/lib/apt/lists/* \
    && mkdir /steamcmd && cd /steamcmd \
    && curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -

# extract local steamcmd into image
# ADD steamcmd_linux.tar.gz /steamcmd

# install CSGO
RUN cd /steamcmd && ./steamcmd.sh +login anonymous +force_install_dir /csgo +app_update 740 validate +app_update 740 +quit

COPY containerfs /

WORKDIR /csgo

CMD ["./start.sh"]
