FROM rbwsam/steamcmd:latest
MAINTAINER rbwsam

# Install the game server
RUN ./steamcmd.sh +login anonymous +force_install_dir /home/steam/dods +app_update 232290 validate +quit

ENTRYPOINT ["/home/steam/dods/srcds_run", "-game", "dod"]
