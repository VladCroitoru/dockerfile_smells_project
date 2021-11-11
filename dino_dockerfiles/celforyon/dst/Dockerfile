FROM celforyon/steamcmd
MAINTAINER Alexis Pereda <alexis@pereda.fr>
LABEL description="Don't Starve Together Server"

ENV APP_ID 343050
ENV APP_DIR /home/steam/apps/dst

USER root
RUN mkdir /conf /mods
RUN chown steam: /conf /mods

USER steam
WORKDIR /home/steam
RUN mkdir apps/dst .klei

RUN bin/steamcmd +login anonymous +force_install_dir $APP_DIR +app_update $APP_ID validate +quit

RUN ln -s /conf .klei/DoNotStarveTogether
RUN mv apps/dst/mods/* /mods && rmdir apps/dst/mods
RUN ln -s /mods apps/dst/mods

COPY launcher /usr/local/bin
COPY runner /usr/local/bin

USER root

ENTRYPOINT ["launcher"]

VOLUME ["/conf", "/mods"]
EXPOSE 10999/udp
