FROM fathosting/steamcmd:latest
MAINTAINER FAT <contact@fat.sh>

RUN ./steamcmd.sh \
      +login anonymous \
      +force_install_dir /home/steam/ark \
      +app_update 376030 validate \
      +quit

COPY lsyncd.conf.lua /etc/lsyncd/
COPY docker-entrypoint.sh /usr/local/bin/

VOLUME ["/home/steam/backup"]
EXPOSE 27015/udp 7777/udp 7778/udp 27020

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["./ShooterGameServer -server -log"]
