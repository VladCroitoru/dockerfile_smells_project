FROM biseque/steamcmd
MAINTAINER biseque <info@biseque.com>

RUN /steamcmd/steamcmd.sh +login anonymous +force_install_dir /data +app_update 600760 +quit

WORKDIR /data
VOLUME ["/data/saves"]

EXPOSE 27500/udp 27015/udp

ENTRYPOINT ["./rocketstation_DedicatedServer.x86_64"]